# Beyerdynamic DT 990 250 ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.9; 25 -5.4; 28 -6.0; 31 -6.5; 34 -6.8; 37 -7.1; 41 -7.4; 45 -7.6; 49 -7.8; 54 -8.0; 60 -8.0; 66 -7.8; 72 -7.6; 79 -7.6; 87 -7.6; 96 -7.8; 106 -7.7; 116 -7.7; 128 -7.5; 141 -7.1; 155 -6.8; 170 -6.5; 187 -6.1; 206 -5.7; 227 -5.2; 249 -4.8; 274 -4.2; 302 -3.6; 332 -3.0; 365 -2.5; 402 -2.0; 442 -2.1; 486 -2.1; 535 -1.7; 588 -1.1; 647 -0.7; 712 -0.5; 783 -0.6; 861 -0.9; 947 -1.4; 1042 -1.8; 1146 -1.8; 1261 -1.8; 1387 -1.8; 1526 -1.8; 1678 -1.8; 1846 -2.1; 2031 -2.6; 2234 -3.0; 2457 -3.1; 2703 -3.2; 2973 -3.6; 3270 -4.0; 3597 -4.3; 3957 -4.7; 4353 -5.7; 4788 -7.1; 5267 -9.2; 5793 -13.0; 6373 -14.6; 7010 -12.1; 7711 -5.8; 8482 -4.2; 9330 -4.2; 10263 -5.5; 11289 -9.3; 12418 -11.2; 13660 -9.2; 15026 -4.6; 16529 -4.2; 18182 -4.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 990 250 ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 990 250 ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 101 Hz   | 0.33 | -4.4 dB  |
| Peaking | 630 Hz   | 0.34 | 4.0 dB   |
| Peaking | 6389 Hz  | 2.51 | -12.5 dB |
| Peaking | 8411 Hz  | 2.06 | 4.5 dB   |
| Peaking | 12365 Hz | 2.46 | -7.7 dB  |
| Peaking | 12 Hz    | 0.58 | 1.6 dB   |
| Peaking | 39 Hz    | 1.62 | -0.9 dB  |
| Peaking | 722 Hz   | 4.27 | 0.7 dB   |
| Peaking | 1073 Hz  | 3.83 | -0.8 dB  |
| Peaking | 15534 Hz | 5.01 | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.0 dB |
| Peaking | 8000 Hz  | 1.41 | -5.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Beyerdynamic%20DT%20990%20250%20ohm/Beyerdynamic%20DT%20990%20250%20ohm.png)