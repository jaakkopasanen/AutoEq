# Sony MDR-1000X Wired Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.8; 25 -7.6; 28 -8.6; 31 -9.5; 34 -10.2; 37 -10.9; 41 -11.6; 45 -12.2; 49 -12.7; 54 -13.2; 60 -13.7; 66 -14.0; 72 -14.0; 79 -13.9; 87 -13.5; 96 -13.2; 106 -13.1; 116 -13.9; 128 -14.0; 141 -12.5; 155 -12.0; 170 -9.6; 187 -10.5; 206 -9.6; 227 -8.3; 249 -7.2; 274 -6.5; 302 -6.1; 332 -5.9; 365 -6.0; 402 -6.1; 442 -6.2; 486 -6.7; 535 -6.8; 588 -6.4; 647 -7.1; 712 -7.1; 783 -5.8; 861 -5.8; 947 -4.7; 1042 -3.3; 1146 -1.7; 1261 -0.5; 1387 -0.5; 1526 -1.5; 1678 -3.0; 1846 -3.6; 2031 -2.9; 2234 -0.9; 2457 -0.5; 2703 -1.5; 2973 -4.7; 3270 -6.9; 3597 -8.5; 3957 -11.1; 4353 -11.2; 4788 -8.3; 5267 -9.5; 5793 -6.7; 6373 -3.2; 7010 -4.0; 7711 -6.2; 8482 -8.5; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-1000X Wired Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-1000X Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 0.88 | -7.0 dB |
| Peaking | 129 Hz  | 1.72 | -4.9 dB |
| Peaking | 1317 Hz | 2.38 | 6.2 dB  |
| Peaking | 2452 Hz | 3    | 6.3 dB  |
| Peaking | 4110 Hz | 3.58 | -6.1 dB |
| Peaking | 201 Hz  | 6.26 | -1.6 dB |
| Peaking | 311 Hz  | 2.02 | 1.3 dB  |
| Peaking | 682 Hz  | 5.34 | -1.4 dB |
| Peaking | 6656 Hz | 4.67 | 7.6 dB  |
| Peaking | 6961 Hz | 1.53 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-1000X%20Wired%20Passive/Sony%20MDR-1000X%20Wired%20Passive.png)