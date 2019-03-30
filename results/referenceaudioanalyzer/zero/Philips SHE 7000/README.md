# Philips SHE 7000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.6; 23 -14.0; 25 -14.3; 28 -14.6; 31 -14.9; 34 -15.0; 37 -15.1; 41 -15.0; 45 -14.9; 49 -14.7; 54 -14.5; 60 -14.2; 66 -13.8; 72 -13.4; 79 -13.0; 87 -12.5; 96 -11.9; 106 -11.3; 116 -10.8; 128 -10.1; 141 -9.5; 155 -8.8; 170 -8.2; 187 -7.4; 206 -6.8; 227 -6.1; 249 -5.5; 274 -4.8; 302 -4.2; 332 -3.6; 365 -2.9; 402 -2.4; 442 -2.4; 486 -2.3; 535 -1.9; 588 -1.4; 647 -1.1; 712 -0.9; 783 -0.7; 861 -0.6; 947 -0.5; 1042 -0.7; 1146 -0.9; 1261 -1.2; 1387 -1.7; 1526 -2.1; 1678 -2.8; 1846 -3.7; 2031 -4.8; 2234 -6.0; 2457 -7.3; 2703 -8.4; 2973 -8.9; 3270 -8.4; 3597 -7.7; 3957 -7.1; 4353 -6.7; 4788 -6.8; 5267 -7.0; 5793 -6.8; 6373 -5.5; 7010 -3.7; 7711 -4.6; 8482 -4.9; 9330 -5.9; 10263 -5.0; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHE 7000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHE 7000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 54 Hz    |  0.21 | -11.5 dB |
| Peaking | 710 Hz   |  0.12 | 6.2 dB   |
| Peaking | 2912 Hz  |  1.08 | -8.8 dB  |
| Peaking | 5387 Hz  |  2.89 | -2.8 dB  |
| Peaking | 9464 Hz  |  3.79 | -1.6 dB  |
| Peaking | 383 Hz   |  4.16 | 0.5 dB   |
| Peaking | 491 Hz   |  4.22 | -0.5 dB  |
| Peaking | 7077 Hz  | 11.72 | 1.3 dB   |
| Peaking | 12891 Hz |  0.42 | -0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.3 dB |
| Peaking | 62 Hz    | 1.41 | -7.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.1 dB   |
| Peaking | 500 Hz   | 1.41 | 2.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Philips%20SHE%207000/Philips%20SHE%207000.png)