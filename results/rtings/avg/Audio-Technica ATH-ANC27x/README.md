# Audio-Technica ATH-ANC27x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -21.7; 23 -21.9; 25 -21.9; 28 -21.4; 31 -20.6; 34 -19.5; 37 -18.6; 41 -18.0; 45 -18.0; 49 -17.5; 54 -16.8; 60 -16.1; 66 -15.6; 72 -15.2; 79 -14.8; 87 -14.5; 96 -14.2; 106 -14.2; 116 -14.1; 128 -14.0; 141 -13.7; 155 -13.5; 170 -13.1; 187 -12.7; 206 -12.3; 227 -11.9; 249 -11.6; 274 -11.3; 302 -10.9; 332 -10.4; 365 -9.9; 402 -9.4; 442 -9.0; 486 -8.6; 535 -8.2; 588 -7.6; 647 -6.7; 712 -5.6; 783 -5.0; 861 -5.6; 947 -5.6; 1042 -6.5; 1146 -6.4; 1261 -6.1; 1387 -4.3; 1526 -1.8; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -1.3; 2973 -3.2; 3270 -1.3; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.3; 5267 -2.4; 5793 -7.2; 6373 -13.7; 7010 -11.6; 7711 -10.9; 8482 -7.7; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.4; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -7.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC27x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC27x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.37 | -15.2 dB |
| Peaking | 179 Hz   | 0.55 | -4.6 dB  |
| Peaking | 1946 Hz  | 1.6  | 5.6 dB   |
| Peaking | 4967 Hz  | 1.14 | 10.2 dB  |
| Peaking | 6499 Hz  | 2.17 | -13.9 dB |
| Peaking | 781 Hz   | 3.71 | 2.2 dB   |
| Peaking | 1269 Hz  | 2    | -2.0 dB  |
| Peaking | 1561 Hz  | 5.42 | 2.4 dB   |
| Peaking | 12659 Hz | 7.98 | -1.9 dB  |
| Peaking | 12804 Hz | 5.13 | -0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -16.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.9 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC27x/Audio-Technica%20ATH-ANC27x.png)