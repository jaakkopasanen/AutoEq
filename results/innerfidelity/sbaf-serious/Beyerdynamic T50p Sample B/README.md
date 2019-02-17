# Beyerdynamic T50p sample B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.0; 41 -1.5; 45 -1.9; 49 -2.3; 54 -2.7; 60 -3.3; 66 -3.7; 72 -4.0; 79 -4.3; 87 -4.7; 96 -5.1; 106 -4.2; 116 -3.6; 128 -4.1; 141 -3.9; 155 -3.4; 170 -3.0; 187 -4.7; 206 -6.4; 227 -7.5; 249 -8.2; 274 -8.3; 302 -8.3; 332 -8.9; 365 -8.9; 402 -8.7; 442 -8.6; 486 -8.6; 535 -8.4; 588 -8.0; 647 -7.8; 712 -6.6; 783 -6.6; 861 -6.8; 947 -6.6; 1042 -6.3; 1146 -5.8; 1261 -5.2; 1387 -4.8; 1526 -4.2; 1678 -3.2; 1846 -1.4; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T50p sample B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.58 | 5.1 dB  |
| Peaking | 56 Hz   | 0.3  | 1.5 dB  |
| Peaking | 161 Hz  | 1.72 | 4.9 dB  |
| Peaking | 281 Hz  | 0.43 | -3.7 dB |
| Peaking | 3207 Hz | 0.63 | 7.0 dB  |
| Peaking | 232 Hz  | 6.68 | -0.4 dB |
| Peaking | 2041 Hz | 2.74 | 3.1 dB  |
| Peaking | 2217 Hz | 0.97 | -1.7 dB |
| Peaking | 6218 Hz | 2.05 | 5.6 dB  |
| Peaking | 7423 Hz | 1.4  | -4.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | 3.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T50p%20sample%20B/Beyerdynamic%20T50p%20sample%20B.png)