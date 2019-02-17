# Audio-Technica ATH-FC700A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.2; 54 -2.2; 60 -2.0; 66 -2.7; 72 -3.8; 79 -4.7; 87 -5.4; 96 -6.0; 106 -6.6; 116 -6.9; 128 -6.7; 141 -5.7; 155 -6.4; 170 -6.7; 187 -6.7; 206 -6.6; 227 -6.6; 249 -6.5; 274 -7.5; 302 -7.4; 332 -7.0; 365 -6.8; 402 -6.7; 442 -6.5; 486 -6.4; 535 -6.2; 588 -6.0; 647 -5.9; 712 -5.6; 783 -5.8; 861 -6.1; 947 -6.4; 1042 -6.5; 1146 -6.7; 1261 -7.1; 1387 -7.3; 1526 -8.2; 1678 -8.7; 1846 -9.3; 2031 -9.6; 2234 -9.4; 2457 -8.4; 2703 -7.1; 2973 -6.0; 3270 -4.9; 3597 -4.2; 3957 -3.6; 4353 -3.3; 4788 -2.8; 5267 -0.8; 5793 -11.3; 6373 -11.5; 7010 -15.9; 7711 -13.9; 8482 -11.4; 9330 -8.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.1; 15026 -10.3; 16529 -10.3; 18182 -8.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-FC700A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-FC700A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.81 | 6.9 dB   |
| Peaking | 2035 Hz  | 2.19 | -3.8 dB  |
| Peaking | 4833 Hz  | 1.66 | 7.1 dB   |
| Peaking | 6932 Hz  | 2.34 | -11.7 dB |
| Peaking | 16072 Hz | 2.18 | -4.5 dB  |
| Peaking | 62 Hz    | 4.1  | 1.4 dB   |
| Peaking | 109 Hz   | 2.53 | -1.3 dB  |
| Peaking | 292 Hz   | 3.53 | -1.2 dB  |
| Peaking | 711 Hz   | 2.6  | 0.9 dB   |
| Peaking | 10920 Hz | 3.22 | 1.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio-Technica%20ATH-FC700A/Audio-Technica%20ATH-FC700A.png)