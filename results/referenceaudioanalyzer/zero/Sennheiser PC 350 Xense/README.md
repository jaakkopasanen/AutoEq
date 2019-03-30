# Sennheiser PC 350 Xense
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -2.3; 25 -2.9; 28 -3.6; 31 -4.2; 34 -4.6; 37 -5.0; 41 -5.4; 45 -5.6; 49 -5.8; 54 -6.0; 60 -6.1; 66 -5.6; 72 -4.8; 79 -4.0; 87 -3.7; 96 -3.6; 106 -2.8; 116 -1.9; 128 -1.2; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -2.4; 274 -4.9; 302 -7.1; 332 -9.1; 365 -10.8; 402 -11.9; 442 -12.4; 486 -12.5; 535 -12.4; 588 -12.2; 647 -12.0; 712 -11.8; 783 -11.4; 861 -10.9; 947 -10.5; 1042 -10.2; 1146 -10.0; 1261 -9.8; 1387 -9.9; 1526 -10.2; 1678 -10.6; 1846 -11.0; 2031 -10.7; 2234 -8.8; 2457 -4.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -2.0; 3957 -2.6; 4353 -3.5; 4788 -5.4; 5267 -6.2; 5793 -5.2; 6373 -5.7; 7010 -8.8; 7711 -11.3; 8482 -11.2; 9330 -9.1; 10263 -8.2; 11289 -9.9; 12418 -11.5; 13660 -10.5; 15026 -8.2; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PC 350 Xense GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PC 350 Xense ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 2.06 | 4.9 dB   |
| Peaking | 209 Hz   | 0.75 | 12.6 dB  |
| Peaking | 408 Hz   | 0.6  | -11.3 dB |
| Peaking | 2033 Hz  | 1.72 | -6.7 dB  |
| Peaking | 2864 Hz  | 1.95 | 10.2 dB  |
| Peaking | 58 Hz    | 3.75 | -1.4 dB  |
| Peaking | 128 Hz   | 4.92 | 0.8 dB   |
| Peaking | 5157 Hz  | 0.95 | 4.5 dB   |
| Peaking | 8320 Hz  | 0.54 | -5.6 dB  |
| Peaking | 22050 Hz | 1.9  | -3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | 5.8 dB  |
| Peaking | 250 Hz   | 1.41 | 4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -7.9 dB |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20PC%20350%20Xense/Sennheiser%20PC%20350%20Xense.png)