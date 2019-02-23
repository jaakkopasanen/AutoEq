# Fostex T20RP Mk3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -1.0; 45 -2.3; 49 -3.8; 54 -5.4; 60 -7.0; 66 -8.5; 72 -9.7; 79 -10.8; 87 -11.6; 96 -12.2; 106 -12.2; 116 -12.1; 128 -11.8; 141 -11.4; 155 -11.0; 170 -10.4; 187 -9.9; 206 -9.3; 227 -9.0; 249 -8.8; 274 -8.4; 302 -8.7; 332 -8.2; 365 -6.9; 402 -6.5; 442 -6.3; 486 -4.3; 535 -4.6; 588 -4.3; 647 -3.6; 712 -4.0; 783 -3.8; 861 -5.3; 947 -5.9; 1042 -6.6; 1146 -7.0; 1261 -5.8; 1387 -7.0; 1526 -5.2; 1678 -5.0; 1846 -5.0; 2031 -3.8; 2234 -4.3; 2457 -4.0; 2703 -4.0; 2973 -4.5; 3270 -4.8; 3597 -5.7; 3957 -7.5; 4353 -8.2; 4788 -6.2; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -10.3; 9330 -12.9; 10263 -10.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex T20RP Mk3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T20RP Mk3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 38 Hz   | 0.52 | 11.0 dB  |
| Peaking | 86 Hz   | 0.56 | -10.8 dB |
| Peaking | 627 Hz  | 1.38 | 3.3 dB   |
| Peaking | 6003 Hz | 3.12 | 7.1 dB   |
| Peaking | 9292 Hz | 3.92 | -7.6 dB  |
| Peaking | 1202 Hz | 1.72 | -2.0 dB  |
| Peaking | 2321 Hz | 0.76 | 2.6 dB   |
| Peaking | 4281 Hz | 4.43 | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T20RP%20Mk3/Fostex%20T20RP%20Mk3.png)