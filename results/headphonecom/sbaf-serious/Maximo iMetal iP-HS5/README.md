# Maximo iMetal iP-HS5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.7; 23 -13.6; 25 -13.4; 28 -13.3; 31 -13.1; 34 -12.9; 37 -12.8; 41 -12.6; 45 -12.4; 49 -12.2; 54 -12.1; 60 -11.9; 66 -11.8; 72 -11.6; 79 -11.4; 87 -11.3; 96 -11.1; 106 -10.8; 116 -10.5; 128 -10.3; 141 -10.0; 155 -9.7; 170 -9.4; 187 -9.0; 206 -8.6; 227 -8.2; 249 -7.7; 274 -7.2; 302 -6.7; 332 -6.3; 365 -6.1; 402 -5.7; 442 -5.3; 486 -5.1; 535 -4.8; 588 -4.6; 647 -4.3; 712 -4.2; 783 -4.3; 861 -4.5; 947 -5.1; 1042 -5.9; 1146 -6.6; 1261 -7.4; 1387 -8.1; 1526 -8.3; 1678 -9.0; 1846 -9.9; 2031 -10.8; 2234 -11.2; 2457 -10.4; 2703 -7.5; 2973 -3.8; 3270 -0.7; 3597 -0.5; 3957 -0.5; 4353 -0.7; 4788 -2.0; 5267 -2.8; 5793 -5.3; 6373 -11.2; 7010 -10.1; 7711 -6.9; 8482 -6.5; 9330 -6.5; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Maximo iMetal iP-HS5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Maximo iMetal iP-HS5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 0.32 | -6.9 dB  |
| Peaking | 121 Hz  | 1.06 | -2.2 dB  |
| Peaking | 2242 Hz | 1.29 | -16.8 dB |
| Peaking | 3091 Hz | 0.56 | 13.7 dB  |
| Peaking | 6708 Hz | 2.59 | -9.6 dB  |
| Peaking | 667 Hz  | 1.23 | 1.8 dB   |
| Peaking | 1327 Hz | 2.72 | -2.0 dB  |
| Peaking | 5235 Hz | 1.54 | 1.7 dB   |
| Peaking | 7792 Hz | 3.87 | 2.9 dB   |
| Peaking | 8486 Hz | 0.79 | -2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Maximo%20iMetal%20iP-HS5/Maximo%20iMetal%20iP-HS5.png)