# Massdrop x E-Mu Purpleheart
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.0; 23 -7.4; 25 -7.8; 28 -8.2; 31 -8.4; 34 -8.7; 37 -8.9; 41 -9.2; 45 -9.4; 49 -9.6; 54 -9.8; 60 -9.9; 66 -10.1; 72 -10.3; 79 -10.5; 87 -10.7; 96 -11.0; 106 -11.2; 116 -11.3; 128 -11.4; 141 -11.3; 155 -11.3; 170 -11.0; 187 -10.8; 206 -10.5; 227 -10.1; 249 -9.7; 274 -9.2; 302 -9.0; 332 -8.6; 365 -8.1; 402 -7.6; 442 -7.2; 486 -7.1; 535 -6.8; 588 -6.2; 647 -6.0; 712 -5.9; 783 -5.7; 861 -5.8; 947 -4.8; 1042 -4.9; 1146 -5.2; 1261 -5.5; 1387 -5.9; 1526 -6.1; 1678 -6.0; 1846 -5.5; 2031 -4.8; 2234 -4.1; 2457 -3.2; 2703 -3.9; 2973 -5.6; 3270 -5.9; 3597 -3.7; 3957 -3.2; 4353 -6.5; 4788 -4.0; 5267 -1.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.6; 9330 -7.5; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x E-Mu Purpleheart GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x E-Mu Purpleheart ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 60 Hz   | 0.53 | -2.4 dB |
| Peaking | 159 Hz  | 0.66 | -3.9 dB |
| Peaking | 934 Hz  | 1.39 | 1.6 dB  |
| Peaking | 2457 Hz | 3.05 | 2.9 dB  |
| Peaking | 5840 Hz | 3.24 | 6.5 dB  |
| Peaking | 1568 Hz | 5.95 | -0.5 dB |
| Peaking | 3265 Hz | 4.13 | -2.4 dB |
| Peaking | 3821 Hz | 3.19 | 4.3 dB  |
| Peaking | 4315 Hz | 7.58 | -3.9 dB |
| Peaking | 9045 Hz | 3.52 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20E-Mu%20Purpleheart/Massdrop%20x%20E-Mu%20Purpleheart.png)