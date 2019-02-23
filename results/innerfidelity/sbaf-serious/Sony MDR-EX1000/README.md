# Sony MDR-EX1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -1.6; 25 -1.9; 28 -2.1; 31 -2.4; 34 -2.5; 37 -2.7; 41 -2.9; 45 -3.2; 49 -3.4; 54 -3.6; 60 -4.0; 66 -4.4; 72 -4.8; 79 -5.1; 87 -5.6; 96 -6.0; 106 -6.3; 116 -6.5; 128 -6.9; 141 -7.2; 155 -7.5; 170 -7.6; 187 -7.6; 206 -7.8; 227 -7.6; 249 -7.7; 274 -7.6; 302 -7.4; 332 -7.3; 365 -7.1; 402 -7.0; 442 -6.6; 486 -6.5; 535 -6.2; 588 -5.6; 647 -5.4; 712 -5.4; 783 -5.0; 861 -5.3; 947 -5.6; 1042 -6.0; 1146 -6.5; 1261 -7.2; 1387 -8.1; 1526 -9.0; 1678 -9.5; 1846 -9.5; 2031 -8.9; 2234 -7.7; 2457 -5.6; 2703 -3.7; 2973 -1.0; 3270 -0.5; 3597 -0.5; 3957 -1.1; 4353 -5.5; 4788 -10.3; 5267 -11.7; 5793 -7.1; 6373 -4.5; 7010 -5.5; 7711 -9.6; 8482 -10.3; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-EX1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-EX1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.77 | 4.9 dB  |
| Peaking | 1859 Hz | 2.31 | -4.5 dB |
| Peaking | 3438 Hz | 1.86 | 7.5 dB  |
| Peaking | 4798 Hz | 5.66 | -3.7 dB |
| Peaking | 5164 Hz | 6.47 | -5.9 dB |
| Peaking | 64 Hz   | 1.7  | 1.0 dB  |
| Peaking | 206 Hz  | 0.77 | -1.5 dB |
| Peaking | 749 Hz  | 1.93 | 1.8 dB  |
| Peaking | 6634 Hz | 5.7  | 2.9 dB  |
| Peaking | 8157 Hz | 5.12 | -5.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-EX1000/Sony%20MDR-EX1000.png)