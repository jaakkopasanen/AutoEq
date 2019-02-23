# Beyerdynamic T50p sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -3.1; 25 -3.7; 28 -4.4; 31 -5.0; 34 -5.5; 37 -6.0; 41 -6.5; 45 -6.9; 49 -7.2; 54 -7.7; 60 -8.3; 66 -8.7; 72 -9.0; 79 -9.3; 87 -9.7; 96 -10.1; 106 -9.2; 116 -8.6; 128 -9.1; 141 -8.9; 155 -8.4; 170 -8.0; 187 -9.6; 206 -11.3; 227 -12.5; 249 -13.2; 274 -13.3; 302 -13.3; 332 -13.8; 365 -13.9; 402 -13.7; 442 -13.5; 486 -13.6; 535 -13.4; 588 -13.0; 647 -12.8; 712 -11.6; 783 -11.6; 861 -11.8; 947 -11.6; 1042 -11.3; 1146 -10.8; 1261 -10.2; 1387 -9.8; 1526 -9.1; 1678 -8.1; 1846 -6.4; 2031 -3.9; 2234 -0.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -10.2; 9330 -11.1; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T50p sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 2.32 | 4.0 dB  |
| Peaking | 498 Hz  | 0.4  | -8.9 dB |
| Peaking | 1438 Hz | 1.16 | -7.1 dB |
| Peaking | 2514 Hz | 0.37 | 9.9 dB  |
| Peaking | 8977 Hz | 3.34 | -8.6 dB |
| Peaking | 66 Hz   | 2.62 | -1.4 dB |
| Peaking | 92 Hz   | 5.57 | -1.6 dB |
| Peaking | 168 Hz  | 5.41 | 2.8 dB  |
| Peaking | 1755 Hz | 6.2  | -0.6 dB |
| Peaking | 3598 Hz | 5.27 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -5.8 dB |
| Peaking | 1000 Hz  | 1.41 | -5.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T50p%20sample%20B/Beyerdynamic%20T50p%20sample%20B.png)