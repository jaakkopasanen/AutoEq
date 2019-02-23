# House of Marley Smile Jamaica
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.0; 23 -14.1; 25 -14.3; 28 -14.4; 31 -14.5; 34 -14.5; 37 -14.6; 41 -14.7; 45 -14.9; 49 -15.0; 54 -15.2; 60 -15.4; 66 -15.6; 72 -15.9; 79 -16.1; 87 -16.4; 96 -16.7; 106 -16.8; 116 -16.8; 128 -16.9; 141 -16.9; 155 -16.8; 170 -16.6; 187 -16.3; 206 -16.0; 227 -15.5; 249 -15.1; 274 -14.6; 302 -13.9; 332 -13.3; 365 -12.5; 402 -11.8; 442 -10.8; 486 -10.2; 535 -9.2; 588 -8.0; 647 -6.8; 712 -5.8; 783 -5.3; 861 -4.7; 947 -4.1; 1042 -3.5; 1146 -3.0; 1261 -3.0; 1387 -4.2; 1526 -6.3; 1678 -7.4; 1846 -6.9; 2031 -5.3; 2234 -3.5; 2457 -1.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.1; 4788 -4.7; 5267 -8.7; 5793 -4.0; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`House of Marley Smile Jamaica GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `House of Marley Smile Jamaica ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.29 | -7.8 dB |
| Peaking | 149 Hz  | 0.83 | -6.3 dB |
| Peaking | 303 Hz  | 1.54 | -4.1 dB |
| Peaking | 3144 Hz | 1.41 | 6.8 dB  |
| Peaking | 6412 Hz | 9.18 | 5.1 dB  |
| Peaking | 475 Hz  | 2.47 | -1.7 dB |
| Peaking | 1225 Hz | 1.09 | 4.6 dB  |
| Peaking | 1701 Hz | 2.54 | -5.5 dB |
| Peaking | 4254 Hz | 6.88 | 2.3 dB  |
| Peaking | 5246 Hz | 8.98 | -5.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.6 dB |
| Peaking | 62 Hz    | 1.41 | -6.4 dB |
| Peaking | 125 Hz   | 1.41 | -8.6 dB |
| Peaking | 250 Hz   | 1.41 | -7.4 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/House%20of%20Marley%20Smile%20Jamaica/House%20of%20Marley%20Smile%20Jamaica.png)