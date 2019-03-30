# IMR R1 (yellow close)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -19.0; 23 -19.0; 25 -18.9; 28 -18.7; 31 -18.6; 34 -18.4; 37 -18.2; 41 -18.0; 45 -17.8; 49 -17.5; 54 -17.2; 60 -16.8; 66 -16.4; 72 -16.0; 79 -15.7; 87 -15.2; 96 -14.7; 106 -14.1; 116 -13.6; 128 -13.0; 141 -12.4; 155 -11.7; 170 -11.1; 187 -10.4; 206 -9.7; 227 -9.2; 249 -8.7; 274 -8.2; 302 -7.5; 332 -6.9; 365 -6.2; 402 -5.4; 442 -4.8; 486 -4.1; 535 -3.5; 588 -2.9; 647 -2.3; 712 -1.7; 783 -1.4; 861 -1.1; 947 -0.9; 1042 -0.7; 1146 -0.5; 1261 -0.7; 1387 -1.0; 1526 -1.4; 1678 -2.1; 1846 -3.1; 2031 -4.4; 2234 -6.3; 2457 -8.7; 2703 -11.3; 2973 -12.5; 3270 -12.0; 3597 -10.2; 3957 -10.1; 4353 -12.4; 4788 -14.7; 5267 -14.8; 5793 -12.2; 6373 -6.8; 7010 -3.9; 7711 -6.1; 8482 -6.3; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`IMR R1 (yellow close) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `IMR R1 (yellow close) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 46 Hz   | 0.25 | -9.6 dB  |
| Peaking | 1748 Hz | 0.32 | 8.2 dB   |
| Peaking | 2898 Hz | 1.46 | -12.4 dB |
| Peaking | 5063 Hz | 3.02 | -11.1 dB |
| Peaking | 17 Hz   | 0.85 | -4.9 dB  |
| Peaking | 37 Hz   | 0.84 | -0.7 dB  |
| Peaking | 5814 Hz | 8.89 | -1.9 dB  |
| Peaking | 6767 Hz | 6.83 | 4.2 dB   |
| Peaking | 9389 Hz | 0.97 | -0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -13.3 dB |
| Peaking | 62 Hz    | 1.41 | -7.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.7 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB   |
| Peaking | 1000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/IMR%20R1%20(yellow%20close)/IMR%20R1%20(yellow%20close).png)