# Alessandro Music Series Two
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.4; 45 -2.4; 49 -3.2; 54 -4.1; 60 -4.8; 66 -5.4; 72 -5.8; 79 -5.9; 87 -5.8; 96 -5.9; 106 -5.6; 116 -5.4; 128 -5.1; 141 -4.8; 155 -4.5; 170 -4.3; 187 -4.2; 206 -3.9; 227 -3.9; 249 -3.6; 274 -3.4; 302 -3.2; 332 -3.0; 365 -2.8; 402 -2.3; 442 -2.3; 486 -2.3; 535 -2.8; 588 -3.3; 647 -3.6; 712 -3.3; 783 -3.3; 861 -3.3; 947 -3.3; 1042 -3.6; 1146 -3.8; 1261 -4.1; 1387 -4.7; 1526 -5.4; 1678 -6.4; 1846 -8.4; 2031 -10.8; 2234 -12.0; 2457 -11.8; 2703 -10.8; 2973 -10.2; 3270 -11.2; 3597 -11.5; 3957 -10.1; 4353 -8.8; 4788 -10.6; 5267 -13.1; 5793 -13.5; 6373 -12.4; 7010 -11.2; 7711 -10.3; 8482 -9.7; 9330 -9.5; 10263 -9.8; 11289 -9.9; 12418 -9.0; 13660 -6.9; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Alessandro Music Series Two GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Alessandro Music Series Two ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 1.09 | 6.8 dB  |
| Peaking | 763 Hz   | 0.27 | 4.3 dB  |
| Peaking | 2421 Hz  | 1.3  | -7.6 dB |
| Peaking | 5853 Hz  | 1.72 | -6.5 dB |
| Peaking | 10875 Hz | 1.96 | -2.9 dB |
| Peaking | 84 Hz    | 2.18 | -1.0 dB |
| Peaking | 632 Hz   | 0.82 | 1.5 dB  |
| Peaking | 658 Hz   | 1.69 | -2.3 dB |
| Peaking | 3569 Hz  | 7.7  | -2.1 dB |
| Peaking | 4380 Hz  | 8.58 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | 2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | -4.0 dB |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Alessandro%20Music%20Series%20Two/Alessandro%20Music%20Series%20Two.png)