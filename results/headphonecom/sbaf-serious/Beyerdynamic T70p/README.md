# Beyerdynamic T70p
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.6; 25 -5.8; 28 -6.0; 31 -6.1; 34 -6.2; 37 -6.4; 41 -6.5; 45 -6.5; 49 -6.6; 54 -6.7; 60 -6.9; 66 -7.0; 72 -7.2; 79 -7.2; 87 -7.4; 96 -7.4; 106 -7.4; 116 -7.4; 128 -7.9; 141 -8.7; 155 -8.8; 170 -7.5; 187 -8.0; 206 -7.7; 227 -7.4; 249 -6.9; 274 -6.7; 302 -6.6; 332 -6.7; 365 -6.8; 402 -7.1; 442 -7.3; 486 -7.2; 535 -6.0; 588 -6.0; 647 -6.2; 712 -6.3; 783 -6.3; 861 -6.4; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -6.8; 1387 -7.3; 1526 -7.9; 1678 -8.0; 1846 -7.1; 2031 -4.3; 2234 -2.1; 2457 -1.7; 2703 -2.4; 2973 -2.7; 3270 -3.0; 3597 -3.0; 3957 -0.5; 4353 -3.6; 4788 -2.3; 5267 -0.5; 5793 -0.5; 6373 -1.3; 7010 -8.5; 7711 -13.5; 8482 -16.3; 9330 -16.6; 10263 -13.7; 11289 -7.2; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T70p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 149 Hz   | 1.28 | -1.8 dB  |
| Peaking | 2459 Hz  | 4.05 | 4.7 dB   |
| Peaking | 3847 Hz  | 2.57 | 4.1 dB   |
| Peaking | 5883 Hz  | 2.74 | 8.7 dB   |
| Peaking | 8683 Hz  | 2.26 | -12.6 dB |
| Peaking | 21 Hz    | 1.68 | 1.1 dB   |
| Peaking | 1621 Hz  | 4.69 | -2.4 dB  |
| Peaking | 10107 Hz | 4.94 | -4.2 dB  |
| Peaking | 11514 Hz | 2.23 | 3.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T70p/Beyerdynamic%20T70p.png)