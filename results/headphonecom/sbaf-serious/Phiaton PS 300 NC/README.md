# Phiaton PS 300 NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -4.9; 25 -6.4; 28 -8.3; 31 -9.6; 34 -10.7; 37 -11.5; 41 -12.2; 45 -12.8; 49 -13.3; 54 -13.8; 60 -14.0; 66 -13.9; 72 -14.6; 79 -16.1; 87 -16.3; 96 -16.6; 106 -16.6; 116 -16.7; 128 -16.9; 141 -16.9; 155 -17.1; 170 -16.9; 187 -16.6; 206 -16.1; 227 -16.1; 249 -15.9; 274 -16.0; 302 -16.0; 332 -16.0; 365 -15.5; 402 -14.4; 442 -12.6; 486 -9.1; 535 -4.5; 588 -1.6; 647 -2.2; 712 -3.1; 783 -4.2; 861 -5.3; 947 -6.1; 1042 -6.8; 1146 -8.2; 1261 -9.0; 1387 -11.6; 1526 -14.5; 1678 -16.7; 1846 -16.6; 2031 -13.9; 2234 -11.6; 2457 -9.5; 2703 -7.5; 2973 -7.6; 3270 -4.0; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.2; 7010 -4.0; 7711 -6.3; 8482 -8.4; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton PS 300 NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 300 NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 85 Hz   | 0.69 | -8.9 dB  |
| Peaking | 189 Hz  | 1.36 | -6.6 dB  |
| Peaking | 337 Hz  | 3.04 | -7.4 dB  |
| Peaking | 1797 Hz | 2.68 | -12.0 dB |
| Peaking | 4598 Hz | 1.49 | 7.5 dB   |
| Peaking | 20 Hz   | 3.67 | 5.3 dB   |
| Peaking | 440 Hz  | 3.3  | -5.1 dB  |
| Peaking | 605 Hz  | 2.22 | 7.7 dB   |
| Peaking | 6270 Hz | 5.97 | 2.8 dB   |
| Peaking | 8429 Hz | 3.6  | -3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -6.9 dB  |
| Peaking | 125 Hz   | 1.41 | -7.9 dB  |
| Peaking | 250 Hz   | 1.41 | -10.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -12.0 dB |
| Peaking | 4000 Hz  | 1.41 | 10.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20PS%20300%20NC/Phiaton%20PS%20300%20NC.png)