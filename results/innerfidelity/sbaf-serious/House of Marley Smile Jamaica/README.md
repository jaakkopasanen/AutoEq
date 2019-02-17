# House of Marley Smile Jamaica
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.7; 23 -16.8; 25 -16.9; 28 -17.0; 31 -17.1; 34 -17.2; 37 -17.3; 41 -17.4; 45 -17.5; 49 -17.7; 54 -17.9; 60 -18.1; 66 -18.3; 72 -18.6; 79 -18.8; 87 -19.1; 96 -19.3; 106 -19.4; 116 -19.5; 128 -19.5; 141 -19.5; 155 -19.4; 170 -19.3; 187 -19.0; 206 -18.7; 227 -18.2; 249 -17.7; 274 -17.2; 302 -16.5; 332 -15.9; 365 -15.2; 402 -14.4; 442 -13.5; 486 -12.8; 535 -11.9; 588 -10.7; 647 -9.4; 712 -8.4; 783 -7.9; 861 -7.3; 947 -6.7; 1042 -6.2; 1146 -5.6; 1261 -5.6; 1387 -6.8; 1526 -8.9; 1678 -10.1; 1846 -9.6; 2031 -7.9; 2234 -6.1; 2457 -3.6; 2703 -1.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.6; 4788 -7.3; 5267 -11.3; 5793 -6.6; 6373 -1.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`House of Marley Smile Jamaica GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `House of Marley Smile Jamaica ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.18 | -9.9 dB |
| Peaking | 163 Hz   | 0.6  | -7.1 dB |
| Peaking | 354 Hz   | 1.14 | -3.9 dB |
| Peaking | 3299 Hz  | 2.62 | 7.3 dB  |
| Peaking | 21886 Hz | 2.3  | 1.6 dB  |
| Peaking | 1581 Hz  | 1.09 | 4.5 dB  |
| Peaking | 1702 Hz  | 2.47 | -8.5 dB |
| Peaking | 4069 Hz  | 7.63 | 3.0 dB  |
| Peaking | 5309 Hz  | 4.65 | -7.2 dB |
| Peaking | 6340 Hz  | 5.56 | 6.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.4 dB |
| Peaking | 62 Hz    | 1.41 | -8.2 dB  |
| Peaking | 125 Hz   | 1.41 | -10.6 dB |
| Peaking | 250 Hz   | 1.41 | -9.3 dB  |
| Peaking | 500 Hz   | 1.41 | -4.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/House%20of%20Marley%20Smile%20Jamaica/House%20of%20Marley%20Smile%20Jamaica.png)