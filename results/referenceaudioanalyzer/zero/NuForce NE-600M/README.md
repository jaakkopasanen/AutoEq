# NuForce NE-600M
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.5; 23 -18.5; 25 -18.6; 28 -18.5; 31 -18.4; 34 -18.3; 37 -18.2; 41 -18.1; 45 -17.9; 49 -17.7; 54 -17.5; 60 -17.1; 66 -16.8; 72 -16.4; 79 -16.0; 87 -15.5; 96 -14.9; 106 -14.1; 116 -13.3; 128 -12.8; 141 -12.8; 155 -12.7; 170 -12.1; 187 -11.4; 206 -10.6; 227 -9.8; 249 -9.1; 274 -8.5; 302 -7.8; 332 -7.1; 365 -6.4; 402 -5.7; 442 -5.0; 486 -4.4; 535 -3.7; 588 -3.0; 647 -2.2; 712 -1.6; 783 -1.2; 861 -0.9; 947 -0.7; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.8; 1526 -1.3; 1678 -2.1; 1846 -3.1; 2031 -4.4; 2234 -6.0; 2457 -8.1; 2703 -9.7; 2973 -10.4; 3270 -10.2; 3597 -9.6; 3957 -9.7; 4353 -10.8; 4788 -11.3; 5267 -9.6; 5793 -5.4; 6373 -1.3; 7010 -3.7; 7711 -5.9; 8482 -6.2; 9330 -6.5; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.2; 16529 -6.2; 18182 -6.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce NE-600M GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce NE-600M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 43 Hz   | 0.07 | -12.6 dB |
| Peaking | 792 Hz  | 0.18 | 10.5 dB  |
| Peaking | 2748 Hz | 1.52 | -8.0 dB  |
| Peaking | 5060 Hz | 1.18 | -9.3 dB  |
| Peaking | 6326 Hz | 3.52 | 9.5 dB   |
| Peaking | 120 Hz  | 2.37 | 1.7 dB   |
| Peaking | 140 Hz  | 1.06 | -0.9 dB  |
| Peaking | 766 Hz  | 3.16 | 0.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -13.0 dB |
| Peaking | 62 Hz    | 1.41 | -7.9 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 4000 Hz  | 1.41 | -5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/NuForce%20NE-600M/NuForce%20NE-600M.png)