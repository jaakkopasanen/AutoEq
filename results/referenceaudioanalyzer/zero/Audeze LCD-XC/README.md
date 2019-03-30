# Audeze LCD-XC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.7; 25 -5.5; 28 -7.1; 31 -8.7; 34 -9.9; 37 -10.2; 41 -9.8; 45 -9.4; 49 -9.4; 54 -9.5; 60 -9.3; 66 -8.9; 72 -8.5; 79 -8.2; 87 -8.5; 96 -8.6; 106 -8.4; 116 -8.0; 128 -7.6; 141 -7.2; 155 -6.5; 170 -5.7; 187 -5.0; 206 -4.1; 227 -2.9; 249 -2.1; 274 -2.3; 302 -3.2; 332 -4.0; 365 -4.6; 402 -4.8; 442 -4.7; 486 -4.7; 535 -5.0; 588 -5.8; 647 -6.5; 712 -6.7; 783 -6.9; 861 -6.9; 947 -6.9; 1042 -7.0; 1146 -7.8; 1261 -9.2; 1387 -9.9; 1526 -9.8; 1678 -9.3; 1846 -8.4; 2031 -6.9; 2234 -4.8; 2457 -2.1; 2703 -0.5; 2973 -2.4; 3270 -8.1; 3597 -12.0; 3957 -13.8; 4353 -14.5; 4788 -13.8; 5267 -11.1; 5793 -8.4; 6373 -9.0; 7010 -8.4; 7711 -6.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -9.2; 13660 -10.9; 15026 -10.5; 16529 -9.3; 18182 -7.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-XC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-XC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 65 Hz    | 0.53 | -2.9 dB  |
| Peaking | 260 Hz   | 1.35 | 4.9 dB   |
| Peaking | 2790 Hz  | 3    | 16.0 dB  |
| Peaking | 3453 Hz  | 1    | -10.8 dB |
| Peaking | 14720 Hz | 2.18 | -4.7 dB  |
| Peaking | 20 Hz    | 3.06 | 3.3 dB   |
| Peaking | 1497 Hz  | 1.83 | -5.0 dB  |
| Peaking | 1732 Hz  | 0.83 | 2.7 dB   |
| Peaking | 4455 Hz  | 4.27 | -3.1 dB  |
| Peaking | 8213 Hz  | 1.5  | 1.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | 4.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.9 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -4.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audeze%20LCD-XC/Audeze%20LCD-XC.png)