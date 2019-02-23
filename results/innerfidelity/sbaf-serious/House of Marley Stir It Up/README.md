# House of Marley Stir It Up
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.9; 23 -10.1; 25 -10.3; 28 -10.6; 31 -10.9; 34 -11.0; 37 -11.1; 41 -11.2; 45 -11.2; 49 -11.0; 54 -10.7; 60 -11.1; 66 -11.5; 72 -11.9; 79 -12.1; 87 -12.5; 96 -13.0; 106 -13.0; 116 -12.8; 128 -13.0; 141 -12.9; 155 -12.5; 170 -12.2; 187 -11.8; 206 -11.4; 227 -10.8; 249 -10.3; 274 -9.9; 302 -9.7; 332 -9.8; 365 -10.0; 402 -10.5; 442 -11.5; 486 -12.4; 535 -12.4; 588 -12.2; 647 -11.9; 712 -11.7; 783 -10.9; 861 -10.4; 947 -9.6; 1042 -8.5; 1146 -7.4; 1261 -6.8; 1387 -6.0; 1526 -5.3; 1678 -4.6; 1846 -3.5; 2031 -2.1; 2234 -1.1; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -4.7; 4788 -5.8; 5267 -4.1; 5793 -2.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`House of Marley Stir It Up GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `House of Marley Stir It Up ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.56 | -3.6 dB |
| Peaking | 124 Hz  | 0.73 | -5.7 dB |
| Peaking | 625 Hz  | 0.97 | -5.8 dB |
| Peaking | 2627 Hz | 1.18 | 5.0 dB  |
| Peaking | 3816 Hz | 0.61 | 2.2 dB  |
| Peaking | 482 Hz  | 9.24 | -0.8 dB |
| Peaking | 3928 Hz | 4.66 | 3.0 dB  |
| Peaking | 4558 Hz | 4.06 | -3.9 dB |
| Peaking | 6301 Hz | 3.81 | 6.0 dB  |
| Peaking | 7239 Hz | 1.34 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -5.1 dB |
| Peaking | 1000 Hz  | 1.41 | -3.2 dB |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/House%20of%20Marley%20Stir%20It%20Up/House%20of%20Marley%20Stir%20It%20Up.png)