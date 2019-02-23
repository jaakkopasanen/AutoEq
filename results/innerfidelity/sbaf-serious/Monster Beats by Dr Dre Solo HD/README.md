# Monster Beats by Dr Dre Solo HD
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.3; 23 -15.2; 25 -15.0; 28 -14.7; 31 -14.3; 34 -14.0; 37 -13.6; 41 -13.2; 45 -12.8; 49 -12.2; 54 -10.8; 60 -9.0; 66 -9.2; 72 -12.7; 79 -16.2; 87 -17.2; 96 -16.5; 106 -15.2; 116 -13.8; 128 -15.3; 141 -15.2; 155 -13.9; 170 -14.0; 187 -13.0; 206 -12.0; 227 -11.0; 249 -11.3; 274 -11.6; 302 -10.5; 332 -9.2; 365 -7.8; 402 -6.1; 442 -4.9; 486 -5.3; 535 -5.3; 588 -5.9; 647 -6.7; 712 -7.5; 783 -7.8; 861 -8.2; 947 -8.2; 1042 -8.3; 1146 -8.2; 1261 -8.2; 1387 -8.3; 1526 -7.8; 1678 -7.2; 1846 -6.6; 2031 -5.6; 2234 -4.9; 2457 -4.0; 2703 -3.4; 2973 -3.4; 3270 -3.6; 3597 -3.7; 3957 -4.4; 4353 -6.1; 4788 -5.9; 5267 -2.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats by Dr Dre Solo HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats by Dr Dre Solo HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.47 | -8.1 dB |
| Peaking | 37 Hz   | 1.96 | -4.6 dB |
| Peaking | 87 Hz   | 3.32 | -7.3 dB |
| Peaking | 150 Hz  | 0.99 | -7.7 dB |
| Peaking | 5945 Hz | 3.12 | 6.3 dB  |
| Peaking | 296 Hz  | 3.29 | -2.8 dB |
| Peaking | 472 Hz  | 1.29 | 4.1 dB  |
| Peaking | 2093 Hz | 0.33 | -5.5 dB |
| Peaking | 2941 Hz | 0.76 | 8.3 dB  |
| Peaking | 4564 Hz | 4.67 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -8.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20by%20Dr%20Dre%20Solo%20HD/Monster%20Beats%20by%20Dr%20Dre%20Solo%20HD.png)