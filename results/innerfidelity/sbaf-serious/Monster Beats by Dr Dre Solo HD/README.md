# Monster Beats by Dr Dre Solo HD
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.4; 23 -13.2; 25 -13.0; 28 -12.7; 31 -12.3; 34 -12.0; 37 -11.7; 41 -11.2; 45 -10.8; 49 -10.2; 54 -8.8; 60 -7.0; 66 -7.2; 72 -10.8; 79 -14.3; 87 -15.2; 96 -14.5; 106 -13.2; 116 -11.8; 128 -13.4; 141 -13.2; 155 -11.9; 170 -12.1; 187 -11.0; 206 -10.0; 227 -9.0; 249 -9.3; 274 -9.6; 302 -8.5; 332 -7.2; 365 -5.8; 402 -4.2; 442 -2.9; 486 -3.3; 535 -3.3; 588 -3.9; 647 -4.7; 712 -5.5; 783 -5.8; 861 -6.2; 947 -6.3; 1042 -6.4; 1146 -6.2; 1261 -6.2; 1387 -6.3; 1526 -5.8; 1678 -5.2; 1846 -4.6; 2031 -3.6; 2234 -2.9; 2457 -2.0; 2703 -1.4; 2973 -1.4; 3270 -1.6; 3597 -1.7; 3957 -2.4; 4353 -4.2; 4788 -3.9; 5267 -1.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats by Dr Dre Solo HD GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats by Dr Dre Solo HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.26 | -6.3 dB |
| Peaking | 112 Hz  | 1    | -7.4 dB |
| Peaking | 2923 Hz | 1.32 | 5.2 dB  |
| Peaking | 5898 Hz | 3.77 | 5.7 dB  |
| Peaking | 64 Hz   | 3.11 | 8.6 dB  |
| Peaking | 81 Hz   | 0.95 | -6.1 dB |
| Peaking | 109 Hz  | 3.27 | 5.5 dB  |
| Peaking | 280 Hz  | 4.28 | -1.9 dB |
| Peaking | 472 Hz  | 2.06 | 4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -7.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 4.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20by%20Dr%20Dre%20Solo%20HD/Monster%20Beats%20by%20Dr%20Dre%20Solo%20HD.png)