# Audio Technica ATH-M50x (Massdrop Velours Earpads)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.6; 25 -3.3; 28 -4.2; 31 -5.0; 34 -5.6; 37 -6.1; 41 -6.5; 45 -6.7; 49 -6.7; 54 -6.6; 60 -6.4; 66 -6.2; 72 -6.1; 79 -5.6; 87 -5.2; 96 -5.5; 106 -6.8; 116 -6.8; 128 -6.8; 141 -7.3; 155 -6.9; 170 -6.3; 187 -5.5; 206 -4.5; 227 -3.1; 249 -1.7; 274 -0.6; 302 -0.5; 332 -1.2; 365 -1.9; 402 -2.9; 442 -3.7; 486 -4.2; 535 -4.5; 588 -4.5; 647 -4.5; 712 -4.5; 783 -4.4; 861 -4.4; 947 -4.5; 1042 -4.3; 1146 -4.7; 1261 -5.2; 1387 -5.3; 1526 -5.4; 1678 -5.5; 1846 -5.6; 2031 -6.0; 2234 -6.9; 2457 -7.8; 2703 -8.1; 2973 -7.7; 3270 -6.1; 3597 -4.4; 3957 -6.6; 4353 -9.8; 4788 -7.6; 5267 -5.3; 5793 -6.1; 6373 -7.9; 7010 -9.0; 7711 -9.1; 8482 -8.4; 9330 -7.7; 10263 -6.8; 11289 -7.2; 12418 -11.9; 13660 -17.9; 15026 -19.3; 16529 -16.2; 18182 -14.6; 20000 -20.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M50x (Massdrop Velours Earpads) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50x (Massdrop Velours Earpads) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 3.28 | 3.3 dB   |
| Peaking | 308 Hz   | 2.17 | 5.4 dB   |
| Peaking | 2660 Hz  | 3.31 | -2.7 dB  |
| Peaking | 14591 Hz | 2.09 | -10.5 dB |
| Peaking | 20333 Hz | 0.31 | -12.9 dB |
| Peaking | 49 Hz    | 2.4  | -1.5 dB  |
| Peaking | 141 Hz   | 2.71 | -2.3 dB  |
| Peaking | 7216 Hz  | 3.26 | -1.4 dB  |
| Peaking | 7539 Hz  | 2.77 | -1.3 dB  |
| Peaking | 10982 Hz | 4.3  | 3.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB   |
| Peaking | 62 Hz    | 1.41 | -0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB  |
| Peaking | 250 Hz   | 1.41 | 4.2 dB   |
| Peaking | 500 Hz   | 1.41 | 1.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -17.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audio%20Technica%20ATH-M50x%20(Massdrop%20Velours%20Earpads)/Audio%20Technica%20ATH-M50x%20(Massdrop%20Velours%20Earpads).png)