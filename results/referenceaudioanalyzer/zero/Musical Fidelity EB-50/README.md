# Musical Fidelity EB-50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.2; 25 -6.7; 28 -7.3; 31 -7.7; 34 -8.0; 37 -8.2; 41 -8.4; 45 -8.6; 49 -8.8; 54 -8.9; 60 -9.0; 66 -9.1; 72 -9.2; 79 -9.2; 87 -9.2; 96 -9.2; 106 -9.2; 116 -9.2; 128 -9.2; 141 -9.2; 155 -9.2; 170 -9.0; 187 -8.9; 206 -8.9; 227 -9.0; 249 -9.2; 274 -8.9; 302 -8.8; 332 -8.6; 365 -8.5; 402 -8.3; 442 -8.1; 486 -7.9; 535 -7.7; 588 -7.5; 647 -7.2; 712 -6.9; 783 -6.7; 861 -6.4; 947 -6.2; 1042 -6.0; 1146 -5.8; 1261 -5.6; 1387 -5.6; 1526 -5.6; 1678 -5.6; 1846 -5.8; 2031 -6.9; 2234 -9.8; 2457 -12.8; 2703 -14.7; 2973 -13.8; 3270 -10.3; 3597 -6.5; 3957 -4.0; 4353 -2.6; 4788 -1.8; 5267 -1.2; 5793 -0.5; 6373 -0.6; 7010 -3.6; 7711 -5.8; 8482 -6.0; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -6.1; 15026 -6.1; 16529 -6.1; 18182 -6.1; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Musical Fidelity EB-50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Musical Fidelity EB-50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 131 Hz  | 0.23 | -3.2 dB  |
| Peaking | 1830 Hz | 0.91 | 2.5 dB   |
| Peaking | 2734 Hz | 2.41 | -11.7 dB |
| Peaking | 5199 Hz | 1.63 | 6.4 dB   |
| Peaking | 19 Hz   | 2.33 | 1.8 dB   |
| Peaking | 3205 Hz | 6.78 | -1.4 dB  |
| Peaking | 3877 Hz | 2.08 | 2.0 dB   |
| Peaking | 6275 Hz | 1.34 | -3.9 dB  |
| Peaking | 6346 Hz | 3.77 | 5.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Musical%20Fidelity%20EB-50/Musical%20Fidelity%20EB-50.png)