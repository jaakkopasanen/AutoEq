# Beyerdynamic T50p sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.1; 37 -1.8; 41 -2.7; 45 -3.5; 49 -4.2; 54 -4.9; 60 -5.7; 66 -6.5; 72 -7.1; 79 -7.5; 87 -7.9; 96 -8.4; 106 -7.7; 116 -7.7; 128 -7.3; 141 -7.5; 155 -6.9; 170 -6.9; 187 -8.6; 206 -10.5; 227 -11.3; 249 -11.6; 274 -11.5; 302 -11.7; 332 -11.7; 365 -11.7; 402 -11.7; 442 -11.5; 486 -11.5; 535 -11.2; 588 -10.6; 647 -10.5; 712 -10.3; 783 -8.9; 861 -8.9; 947 -9.1; 1042 -8.9; 1146 -8.6; 1261 -8.4; 1387 -8.5; 1526 -8.8; 1678 -8.9; 1846 -8.2; 2031 -7.0; 2234 -5.1; 2457 -2.4; 2703 -1.2; 2973 -1.0; 3270 -0.9; 3597 -1.1; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.7; 6373 -2.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.5; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T50p sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 1.22 | 6.8 dB  |
| Peaking | 242 Hz  | 3.64 | -2.1 dB |
| Peaking | 430 Hz  | 0.62 | -5.2 dB |
| Peaking | 1711 Hz | 2.01 | -4.0 dB |
| Peaking | 3672 Hz | 0.83 | 7.1 dB  |
| Peaking | 41 Hz   | 2.42 | 0.9 dB  |
| Peaking | 88 Hz   | 2.19 | -1.6 dB |
| Peaking | 164 Hz  | 5.79 | 1.9 dB  |
| Peaking | 6123 Hz | 2.14 | 4.9 dB  |
| Peaking | 7282 Hz | 1.1  | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -4.2 dB |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T50p%20sample%20A/Beyerdynamic%20T50p%20sample%20A.png)