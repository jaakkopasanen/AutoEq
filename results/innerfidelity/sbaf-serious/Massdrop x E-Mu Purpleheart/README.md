# Massdrop x E-Mu Purpleheart
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.8; 25 -9.2; 28 -9.6; 31 -9.9; 34 -10.1; 37 -10.3; 41 -10.6; 45 -10.8; 49 -11.0; 54 -11.2; 60 -11.4; 66 -11.5; 72 -11.7; 79 -11.9; 87 -12.2; 96 -12.4; 106 -12.6; 116 -12.7; 128 -12.8; 141 -12.7; 155 -12.7; 170 -12.4; 187 -12.3; 206 -11.9; 227 -11.5; 249 -11.1; 274 -10.6; 302 -10.4; 332 -10.0; 365 -9.5; 402 -9.0; 442 -8.6; 486 -8.5; 535 -8.2; 588 -7.6; 647 -7.4; 712 -7.4; 783 -7.1; 861 -7.2; 947 -6.2; 1042 -6.3; 1146 -6.6; 1261 -6.9; 1387 -7.3; 1526 -7.5; 1678 -7.4; 1846 -6.9; 2031 -6.3; 2234 -5.5; 2457 -4.6; 2703 -5.3; 2973 -7.0; 3270 -7.3; 3597 -5.2; 3957 -4.6; 4353 -7.9; 4788 -5.4; 5267 -3.2; 5793 -0.5; 6373 -1.3; 7010 -3.7; 7711 -5.9; 8482 -7.8; 9330 -8.9; 10263 -7.8; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x E-Mu Purpleheart GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x E-Mu Purpleheart ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.58 | -2.5 dB |
| Peaking | 147 Hz  | 0.45 | -6.1 dB |
| Peaking | 6074 Hz | 3.57 | 6.3 dB  |
| Peaking | 9219 Hz | 3.65 | -3.4 dB |
| Peaking | 882 Hz  | 3.15 | -0.4 dB |
| Peaking | 983 Hz  | 4.12 | 1.1 dB  |
| Peaking | 1594 Hz | 2.46 | -1.3 dB |
| Peaking | 2512 Hz | 3.63 | 2.1 dB  |
| Peaking | 3055 Hz | 5.55 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20E-Mu%20Purpleheart/Massdrop%20x%20E-Mu%20Purpleheart.png)