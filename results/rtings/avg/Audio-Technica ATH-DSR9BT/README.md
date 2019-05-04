# Audio-Technica ATH-DSR9BT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -1.8; 25 -2.5; 28 -3.5; 31 -4.3; 34 -4.9; 37 -5.4; 41 -5.8; 45 -6.1; 49 -6.4; 54 -6.8; 60 -7.3; 66 -7.8; 72 -8.4; 79 -9.3; 87 -9.7; 96 -10.0; 106 -10.6; 116 -10.7; 128 -11.0; 141 -11.1; 155 -10.8; 170 -10.4; 187 -9.7; 206 -8.6; 227 -7.0; 249 -4.8; 274 -1.6; 302 -0.5; 332 -0.5; 365 -0.5; 402 -1.7; 442 -4.0; 486 -4.7; 535 -4.9; 588 -4.7; 647 -4.9; 712 -5.1; 783 -5.3; 861 -5.1; 947 -4.8; 1042 -5.2; 1146 -5.2; 1261 -5.2; 1387 -5.9; 1526 -6.9; 1678 -7.6; 1846 -9.0; 2031 -9.8; 2234 -10.9; 2457 -10.5; 2703 -10.2; 2973 -9.8; 3270 -9.2; 3597 -8.3; 3957 -8.5; 4353 -8.7; 4788 -6.1; 5267 -5.6; 5793 -6.1; 6373 -7.8; 7010 -8.9; 7711 -8.2; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -7.2; 12418 -11.2; 13660 -11.6; 15026 -10.2; 16529 -8.2; 18182 -7.8; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-DSR9BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-DSR9BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 211 Hz   | 0.48 | -17.6 dB |
| Peaking | 293 Hz   | 0.7  | 20.9 dB  |
| Peaking | 2487 Hz  | 1.66 | -4.7 dB  |
| Peaking | 13837 Hz | 1.81 | -5.5 dB  |
| Peaking | 17 Hz    | 0.81 | 6.7 dB   |
| Peaking | 55 Hz    | 1.85 | 1.3 dB   |
| Peaking | 488 Hz   | 5.81 | -1.5 dB  |
| Peaking | 7162 Hz  | 3.36 | -5.3 dB  |
| Peaking | 7301 Hz  | 1.5  | 3.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | 3.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -4.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-DSR9BT/Audio-Technica%20ATH-DSR9BT.png)