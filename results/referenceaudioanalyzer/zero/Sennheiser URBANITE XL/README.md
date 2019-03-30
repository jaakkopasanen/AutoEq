# Sennheiser URBANITE XL
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.1; 23 -14.3; 25 -14.4; 28 -14.6; 31 -14.6; 34 -14.7; 37 -14.7; 41 -14.6; 45 -14.7; 49 -14.7; 54 -14.6; 60 -14.2; 66 -13.9; 72 -13.7; 79 -13.7; 87 -14.0; 96 -14.4; 106 -14.6; 116 -14.7; 128 -15.1; 141 -15.3; 155 -15.0; 170 -14.3; 187 -13.3; 206 -11.9; 227 -10.3; 249 -8.8; 274 -8.0; 302 -7.9; 332 -8.1; 365 -7.6; 402 -7.0; 442 -6.6; 486 -5.7; 535 -4.0; 588 -2.0; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.9; 1042 -1.7; 1146 -2.0; 1261 -2.0; 1387 -2.3; 1526 -2.7; 1678 -3.3; 1846 -3.9; 2031 -4.3; 2234 -4.0; 2457 -3.6; 2703 -3.6; 2973 -3.4; 3270 -3.3; 3597 -2.9; 3957 -1.7; 4353 -1.3; 4788 -6.9; 5267 -11.4; 5793 -12.8; 6373 -13.2; 7010 -12.2; 7711 -8.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -7.4; 12418 -9.6; 13660 -9.6; 15026 -6.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser URBANITE XL GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser URBANITE XL ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.31 | -7.9 dB  |
| Peaking | 149 Hz   | 1.03 | -6.3 dB  |
| Peaking | 859 Hz   | 0.92 | 6.5 dB   |
| Peaking | 4308 Hz  | 1.47 | 9.9 dB   |
| Peaking | 5648 Hz  | 1.79 | -12.7 dB |
| Peaking | 263 Hz   | 3.87 | 1.6 dB   |
| Peaking | 482 Hz   | 1.19 | -1.8 dB  |
| Peaking | 624 Hz   | 3.56 | 2.9 dB   |
| Peaking | 8874 Hz  | 3.99 | 2.0 dB   |
| Peaking | 13034 Hz | 3.74 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.6 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -8.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20URBANITE%20XL/Sennheiser%20URBANITE%20XL.png)