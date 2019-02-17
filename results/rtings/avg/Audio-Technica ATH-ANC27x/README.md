# Audio-Technica ATH-ANC27x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -22.0; 23 -22.2; 25 -22.2; 28 -21.7; 31 -20.9; 34 -19.9; 37 -18.9; 41 -18.4; 45 -18.3; 49 -17.8; 54 -17.1; 60 -16.4; 66 -16.0; 72 -15.5; 79 -15.2; 87 -14.8; 96 -14.5; 106 -14.5; 116 -14.5; 128 -14.3; 141 -14.0; 155 -13.8; 170 -13.4; 187 -13.0; 206 -12.6; 227 -12.3; 249 -11.9; 274 -11.6; 302 -11.2; 332 -10.7; 365 -10.2; 402 -9.8; 442 -9.3; 486 -8.9; 535 -8.5; 588 -7.9; 647 -7.1; 712 -5.9; 783 -5.4; 861 -5.9; 947 -6.0; 1042 -6.9; 1146 -6.8; 1261 -6.4; 1387 -4.7; 1526 -2.1; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -1.6; 2973 -3.5; 3270 -1.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.6; 5267 -2.7; 5793 -7.5; 6373 -14.0; 7010 -11.9; 7711 -11.2; 8482 -8.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.8; 13660 -6.6; 15026 -6.5; 16529 -6.7; 18182 -7.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC27x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC27x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.38 | -15.4 dB |
| Peaking | 179 Hz   | 0.51 | -4.9 dB  |
| Peaking | 1949 Hz  | 1.78 | 5.7 dB   |
| Peaking | 4859 Hz  | 1.14 | 9.8 dB   |
| Peaking | 6550 Hz  | 2.19 | -13.6 dB |
| Peaking | 784 Hz   | 3.56 | 2.2 dB   |
| Peaking | 1276 Hz  | 1.71 | -2.0 dB  |
| Peaking | 1574 Hz  | 5.18 | 2.6 dB   |
| Peaking | 17512 Hz | 3.59 | -1.6 dB  |
| Peaking | 17936 Hz | 3.48 | -0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -16.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB  |
| Peaking | 125 Hz   | 1.41 | -5.8 dB  |
| Peaking | 250 Hz   | 1.41 | -4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -5.2 dB  |
| Peaking | 16000 Hz | 1.41 | 0.0 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC27x/Audio-Technica%20ATH-ANC27x.png)