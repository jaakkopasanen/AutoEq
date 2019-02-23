# Phiaton PS 300 NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -2.4; 25 -4.0; 28 -5.8; 31 -7.1; 34 -8.2; 37 -9.0; 41 -9.7; 45 -10.3; 49 -10.9; 54 -11.3; 60 -11.5; 66 -11.5; 72 -12.2; 79 -13.6; 87 -13.9; 96 -14.1; 106 -14.1; 116 -14.2; 128 -14.5; 141 -14.5; 155 -14.6; 170 -14.5; 187 -14.1; 206 -13.6; 227 -13.6; 249 -13.4; 274 -13.5; 302 -13.5; 332 -13.5; 365 -13.0; 402 -11.9; 442 -10.1; 486 -6.6; 535 -2.0; 588 -0.7; 647 -0.7; 712 -0.7; 783 -1.7; 861 -2.9; 947 -3.6; 1042 -4.3; 1146 -5.7; 1261 -6.5; 1387 -9.1; 1526 -12.1; 1678 -14.2; 1846 -14.2; 2031 -11.4; 2234 -9.2; 2457 -7.0; 2703 -5.0; 2973 -5.2; 3270 -1.6; 3597 -0.7; 3957 -0.7; 4353 -0.7; 4788 -0.7; 5267 -0.7; 5793 -0.8; 6373 -1.3; 7010 -4.2; 7711 -6.4; 8482 -6.7; 9330 -6.7; 10263 -6.7; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 300 NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 300 NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 2.29 | 8.0 dB   |
| Peaking | 158 Hz  | 0.43 | -12.9 dB |
| Peaking | 352 Hz  | 1.77 | -9.1 dB  |
| Peaking | 954 Hz  | 0.18 | 13.0 dB  |
| Peaking | 1720 Hz | 1.39 | -19.8 dB |
| Peaking | 457 Hz  | 4.34 | -3.8 dB  |
| Peaking | 560 Hz  | 2.42 | 3.8 dB   |
| Peaking | 973 Hz  | 2.04 | -1.5 dB  |
| Peaking | 6033 Hz | 1.32 | 6.6 dB   |
| Peaking | 7496 Hz | 1.05 | -6.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -8.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.9 dB |
| Peaking | 4000 Hz  | 1.41 | 9.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20PS%20300%20NC/Phiaton%20PS%20300%20NC.png)