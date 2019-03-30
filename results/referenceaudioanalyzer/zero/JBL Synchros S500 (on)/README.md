# JBL Synchros S500 (on)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.1; 23 -12.7; 25 -13.5; 28 -14.9; 31 -16.6; 34 -18.2; 37 -19.2; 41 -19.2; 45 -17.9; 49 -16.6; 54 -15.3; 60 -13.8; 66 -13.0; 72 -13.7; 79 -14.9; 87 -14.9; 96 -13.9; 106 -12.6; 116 -12.2; 128 -12.3; 141 -11.5; 155 -10.6; 170 -10.1; 187 -9.5; 206 -8.7; 227 -8.6; 249 -8.6; 274 -8.6; 302 -8.3; 332 -7.2; 365 -5.9; 402 -4.3; 442 -2.7; 486 -1.1; 535 -0.5; 588 -0.5; 647 -0.5; 712 -0.5; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -2.9; 1146 -4.8; 1261 -4.8; 1387 -3.4; 1526 -1.6; 1678 -1.7; 1846 -4.2; 2031 -6.9; 2234 -8.7; 2457 -9.8; 2703 -10.4; 2973 -10.6; 3270 -9.7; 3597 -8.7; 3957 -10.0; 4353 -11.9; 4788 -12.7; 5267 -12.5; 5793 -12.5; 6373 -12.5; 7010 -11.1; 7711 -7.2; 8482 -6.5; 9330 -6.5; 10263 -7.1; 11289 -8.7; 12418 -10.0; 13660 -10.6; 15026 -9.1; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Synchros S500 (on) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Synchros S500 (on) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 2.23 | -6.5 dB |
| Peaking | 59 Hz    | 0.27 | -7.2 dB |
| Peaking | 661 Hz   | 0.96 | 7.8 dB  |
| Peaking | 1618 Hz  | 4.55 | 5.8 dB  |
| Peaking | 4510 Hz  | 0.62 | -5.5 dB |
| Peaking | 2619 Hz  | 3.75 | -1.4 dB |
| Peaking | 3637 Hz  | 5.26 | 3.1 dB  |
| Peaking | 6733 Hz  | 1.72 | -5.0 dB |
| Peaking | 8102 Hz  | 1.72 | 6.3 dB  |
| Peaking | 13372 Hz | 2    | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.1 dB |
| Peaking | 62 Hz    | 1.41 | -6.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.2 dB  |
| Peaking | 250 Hz   | 1.41 | -2.7 dB  |
| Peaking | 500 Hz   | 1.41 | 5.6 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 4000 Hz  | 1.41 | -6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -2.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/JBL%20Synchros%20S500%20(on)/JBL%20Synchros%20S500%20(on).png)