# iMetal iM590
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.0; 23 -13.9; 25 -13.9; 28 -13.8; 31 -13.8; 34 -13.7; 37 -13.7; 41 -13.6; 45 -13.6; 49 -13.5; 54 -13.5; 60 -13.5; 66 -13.4; 72 -13.3; 79 -13.4; 87 -13.4; 96 -13.5; 106 -13.3; 116 -13.1; 128 -12.9; 141 -12.7; 155 -12.4; 170 -12.0; 187 -11.6; 206 -11.2; 227 -10.7; 249 -10.2; 274 -9.7; 302 -9.2; 332 -8.6; 365 -8.1; 402 -7.6; 442 -7.0; 486 -6.7; 535 -6.4; 588 -5.8; 647 -5.6; 712 -5.5; 783 -5.4; 861 -5.7; 947 -6.1; 1042 -6.7; 1146 -7.1; 1261 -7.5; 1387 -8.2; 1526 -9.0; 1678 -10.2; 1846 -11.2; 2031 -12.0; 2234 -12.4; 2457 -10.7; 2703 -8.0; 2973 -4.3; 3270 -1.5; 3597 -0.5; 3957 -1.7; 4353 -5.6; 4788 -9.6; 5267 -9.9; 5793 -9.4; 6373 -8.9; 7010 -5.4; 7711 -6.2; 8482 -6.5; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iMetal iM590 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iMetal iM590 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.26 | -7.2 dB |
| Peaking | 148 Hz  | 0.86 | -3.6 dB |
| Peaking | 2207 Hz | 1.9  | -8.7 dB |
| Peaking | 3659 Hz | 1.57 | 10.6 dB |
| Peaking | 5042 Hz | 2.21 | -8.1 dB |
| Peaking | 274 Hz  | 2.1  | -0.8 dB |
| Peaking | 707 Hz  | 1.5  | 1.8 dB  |
| Peaking | 1583 Hz | 3    | -0.9 dB |
| Peaking | 6311 Hz | 8.81 | -1.5 dB |
| Peaking | 7084 Hz | 7.44 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -5.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/iMetal%20iM590/iMetal%20iM590.png)