# Beyerdynamic DT 240 Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.8; 25 -8.2; 28 -8.7; 31 -9.1; 34 -9.5; 37 -9.7; 41 -10.0; 45 -10.2; 49 -10.4; 54 -10.6; 60 -10.6; 66 -10.7; 72 -10.7; 79 -10.2; 87 -9.4; 96 -10.7; 106 -11.9; 116 -11.9; 128 -11.1; 141 -11.1; 155 -11.5; 170 -11.0; 187 -11.2; 206 -10.9; 227 -10.0; 249 -9.5; 274 -8.6; 302 -7.7; 332 -6.7; 365 -6.3; 402 -7.1; 442 -7.1; 486 -7.2; 535 -6.9; 588 -6.5; 647 -6.5; 712 -6.8; 783 -6.7; 861 -6.8; 947 -6.6; 1042 -6.2; 1146 -6.4; 1261 -6.7; 1387 -7.4; 1526 -8.4; 1678 -9.0; 1846 -9.3; 2031 -9.1; 2234 -8.7; 2457 -7.3; 2703 -6.1; 2973 -4.6; 3270 -3.0; 3597 -0.7; 3957 -4.1; 4353 -4.4; 4788 -1.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 240 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 240 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 50 Hz   | 0.69 | -3.4 dB |
| Peaking | 153 Hz  | 0.98 | -4.4 dB |
| Peaking | 3541 Hz | 6.56 | 5.2 dB  |
| Peaking | 5585 Hz | 2.84 | 6.9 dB  |
| Peaking | 15 Hz   | 1.4  | 0.6 dB  |
| Peaking | 807 Hz  | 2.05 | -1.0 dB |
| Peaking | 1619 Hz | 0.48 | 2.1 dB  |
| Peaking | 1866 Hz | 1.56 | -5.2 dB |
| Peaking | 8995 Hz | 3.43 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20240%20Pro/Beyerdynamic%20DT%20240%20Pro.png)