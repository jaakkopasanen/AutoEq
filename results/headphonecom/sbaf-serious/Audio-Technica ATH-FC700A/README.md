# Audio-Technica ATH-FC700A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.8; 54 -1.5; 60 -1.3; 66 -2.1; 72 -3.2; 79 -4.0; 87 -4.8; 96 -5.4; 106 -6.0; 116 -6.3; 128 -6.1; 141 -5.1; 155 -5.7; 170 -6.0; 187 -6.0; 206 -5.9; 227 -5.9; 249 -5.9; 274 -6.8; 302 -6.8; 332 -6.3; 365 -6.2; 402 -6.1; 442 -5.9; 486 -5.7; 535 -5.6; 588 -5.3; 647 -5.3; 712 -5.0; 783 -5.2; 861 -5.5; 947 -5.8; 1042 -5.9; 1146 -6.1; 1261 -6.5; 1387 -6.7; 1526 -7.6; 1678 -8.1; 1846 -8.7; 2031 -9.0; 2234 -8.8; 2457 -7.8; 2703 -6.5; 2973 -5.4; 3270 -4.3; 3597 -3.6; 3957 -3.0; 4353 -2.6; 4788 -2.2; 5267 -1.2; 5793 -10.6; 6373 -10.9; 7010 -15.2; 7711 -13.3; 8482 -10.8; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -9.7; 16529 -9.6; 18182 -7.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-FC700A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-FC700A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.65 | 6.7 dB   |
| Peaking | 2091 Hz  | 2.55 | -3.6 dB  |
| Peaking | 4833 Hz  | 1.32 | 7.4 dB   |
| Peaking | 6907 Hz  | 2.29 | -11.9 dB |
| Peaking | 16219 Hz | 2.34 | -3.9 dB  |
| Peaking | 34 Hz    | 2.93 | -0.5 dB  |
| Peaking | 62 Hz    | 3.55 | 1.4 dB   |
| Peaking | 106 Hz   | 3.33 | -1.2 dB  |
| Peaking | 699 Hz   | 1.78 | 1.5 dB   |
| Peaking | 10458 Hz | 4.19 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.2 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio-Technica%20ATH-FC700A/Audio-Technica%20ATH-FC700A.png)