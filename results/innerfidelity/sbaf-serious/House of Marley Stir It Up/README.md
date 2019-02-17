# House of Marley Stir It Up
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.7; 25 -8.0; 28 -8.3; 31 -8.5; 34 -8.7; 37 -8.8; 41 -8.9; 45 -8.8; 49 -8.6; 54 -8.4; 60 -8.7; 66 -9.2; 72 -9.5; 79 -9.7; 87 -10.1; 96 -10.6; 106 -10.6; 116 -10.5; 128 -10.7; 141 -10.5; 155 -10.1; 170 -9.8; 187 -9.5; 206 -9.1; 227 -8.4; 249 -7.9; 274 -7.5; 302 -7.3; 332 -7.4; 365 -7.6; 402 -8.1; 442 -9.2; 486 -10.0; 535 -10.0; 588 -9.8; 647 -9.6; 712 -9.3; 783 -8.6; 861 -8.0; 947 -7.2; 1042 -6.1; 1146 -5.1; 1261 -4.5; 1387 -3.6; 1526 -2.9; 1678 -2.2; 1846 -1.1; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.3; 4788 -3.5; 5267 -1.7; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`House of Marley Stir It Up GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `House of Marley Stir It Up ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.92 | -1.7 dB |
| Peaking | 117 Hz  | 0.92 | -4.1 dB |
| Peaking | 628 Hz  | 1.28 | -4.2 dB |
| Peaking | 2560 Hz | 0.73 | 6.7 dB  |
| Peaking | 6001 Hz | 4.77 | 4.3 dB  |
| Peaking | 326 Hz  | 3.13 | 0.8 dB  |
| Peaking | 479 Hz  | 7.24 | -1.0 dB |
| Peaking | 2647 Hz | 5.46 | -0.7 dB |
| Peaking | 3935 Hz | 7.01 | 1.5 dB  |
| Peaking | 8598 Hz | 2.68 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | -3.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/House%20of%20Marley%20Stir%20It%20Up/House%20of%20Marley%20Stir%20It%20Up.png)