# Audio Technica ATH-M50x (Massdrop Velours Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.5; 25 -2.3; 28 -3.3; 31 -4.2; 34 -4.9; 37 -5.5; 41 -6.0; 45 -6.2; 49 -6.3; 54 -6.3; 60 -6.1; 66 -5.9; 72 -5.8; 79 -5.1; 87 -5.0; 96 -5.4; 106 -6.6; 116 -6.5; 128 -6.6; 141 -7.0; 155 -6.7; 170 -6.1; 187 -5.3; 206 -4.4; 227 -3.0; 249 -1.7; 274 -0.6; 302 -0.5; 332 -1.2; 365 -1.9; 402 -2.9; 442 -3.7; 486 -4.2; 535 -4.5; 588 -4.5; 647 -4.5; 712 -4.5; 783 -4.4; 861 -4.5; 947 -4.5; 1042 -4.4; 1146 -4.7; 1261 -5.1; 1387 -5.2; 1526 -5.3; 1678 -5.3; 1846 -5.5; 2031 -5.9; 2234 -6.8; 2457 -7.8; 2703 -8.1; 2973 -7.8; 3270 -6.3; 3597 -4.6; 3957 -6.7; 4353 -10.2; 4788 -7.8; 5267 -5.7; 5793 -6.0; 6373 -7.0; 7010 -8.5; 7711 -8.8; 8482 -8.0; 9330 -7.3; 10263 -6.6; 11289 -7.2; 12418 -11.6; 13660 -17.1; 15026 -18.6; 16529 -15.7; 18182 -14.1; 20000 -19.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M50x (Massdrop Velours Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50x (Massdrop Velours Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 2.92 | 5.0 dB   |
| Peaking | 306 Hz   | 2.18 | 5.3 dB   |
| Peaking | 2707 Hz  | 2.79 | -2.7 dB  |
| Peaking | 14678 Hz | 1.78 | -10.9 dB |
| Peaking | 20308 Hz | 0.44 | -13.2 dB |
| Peaking | 18 Hz    | 1.9  | 0.7 dB   |
| Peaking | 140 Hz   | 2.08 | -2.1 dB  |
| Peaking | 2851 Hz  | 0.1  | 0.6 dB   |
| Peaking | 4394 Hz  | 7.85 | -5.1 dB  |
| Peaking | 7397 Hz  | 4.09 | -3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB   |
| Peaking | 62 Hz    | 1.41 | -0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB  |
| Peaking | 250 Hz   | 1.41 | 4.2 dB   |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -16.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audio%20Technica%20ATH-M50x%20(Massdrop%20Velours%20Earpads)/Audio%20Technica%20ATH-M50x%20(Massdrop%20Velours%20Earpads).png)