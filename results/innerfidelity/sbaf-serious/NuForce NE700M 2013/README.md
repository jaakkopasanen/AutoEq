# NuForce NE700M 2013
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.5; 23 -15.3; 25 -15.1; 28 -14.8; 31 -14.5; 34 -14.1; 37 -13.9; 41 -13.6; 45 -13.3; 49 -13.0; 54 -12.7; 60 -12.3; 66 -12.1; 72 -11.9; 79 -11.7; 87 -11.5; 96 -11.3; 106 -11.0; 116 -10.6; 128 -10.4; 141 -9.9; 155 -9.7; 170 -9.2; 187 -8.8; 206 -8.4; 227 -7.8; 249 -7.3; 274 -6.8; 302 -6.3; 332 -5.7; 365 -5.2; 402 -4.7; 442 -4.2; 486 -3.9; 535 -3.5; 588 -2.8; 647 -2.7; 712 -2.6; 783 -2.3; 861 -2.6; 947 -2.9; 1042 -3.5; 1146 -4.0; 1261 -4.6; 1387 -5.5; 1526 -6.6; 1678 -7.4; 1846 -7.9; 2031 -8.4; 2234 -9.3; 2457 -10.0; 2703 -10.4; 2973 -8.5; 3270 -5.5; 3597 -3.8; 3957 -4.4; 4353 -6.8; 4788 -7.9; 5267 -6.5; 5793 -3.2; 6373 -0.5; 7010 -3.1; 7711 -5.3; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -7.9; 16529 -6.1; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce NE700M 2013 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce NE700M 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.55 | -8.1 dB |
| Peaking | 59 Hz    | 0.29 | -5.6 dB |
| Peaking | 686 Hz   | 0.8  | 3.9 dB  |
| Peaking | 2321 Hz  | 1.91 | -5.0 dB |
| Peaking | 6390 Hz  | 6.37 | 5.9 dB  |
| Peaking | 1628 Hz  | 4.09 | -1.4 dB |
| Peaking | 2850 Hz  | 3.73 | -4.9 dB |
| Peaking | 3478 Hz  | 1.41 | 4.9 dB  |
| Peaking | 4690 Hz  | 3.49 | -4.7 dB |
| Peaking | 15349 Hz | 4.48 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NuForce%20NE700M%202013/NuForce%20NE700M%202013.png)