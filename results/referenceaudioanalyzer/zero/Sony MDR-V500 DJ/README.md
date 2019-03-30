# Sony MDR-V500 DJ
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.9; 155 -1.4; 170 -1.9; 187 -2.4; 206 -2.7; 227 -3.0; 249 -3.0; 274 -3.2; 302 -3.8; 332 -4.2; 365 -4.5; 402 -4.8; 442 -5.0; 486 -5.3; 535 -5.4; 588 -5.7; 647 -6.1; 712 -6.4; 783 -6.6; 861 -6.6; 947 -7.0; 1042 -7.6; 1146 -8.0; 1261 -8.4; 1387 -9.1; 1526 -9.8; 1678 -10.1; 1846 -10.1; 2031 -9.8; 2234 -9.8; 2457 -9.8; 2703 -9.9; 2973 -10.5; 3270 -11.0; 3597 -11.1; 3957 -10.8; 4353 -10.4; 4788 -9.7; 5267 -8.9; 5793 -9.2; 6373 -10.3; 7010 -11.2; 7711 -10.6; 8482 -7.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -6.7; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-V500 DJ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V500 DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.43 | 5.0 dB  |
| Peaking | 109 Hz  | 0.41 | 5.2 dB  |
| Peaking | 1678 Hz | 1.36 | -3.1 dB |
| Peaking | 3634 Hz | 1.37 | -4.2 dB |
| Peaking | 7074 Hz | 3.88 | -4.4 dB |
| Peaking | 133 Hz  | 4.76 | 0.5 dB  |
| Peaking | 204 Hz  | 2.08 | -0.5 dB |
| Peaking | 266 Hz  | 4.7  | 0.5 dB  |
| Peaking | 7878 Hz | 7.62 | -1.6 dB |
| Peaking | 8787 Hz | 3.39 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | 5.0 dB  |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | -3.7 dB |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20MDR-V500%20DJ/Sony%20MDR-V500%20DJ.png)