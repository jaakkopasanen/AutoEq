# AAW A3H V2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.5; 25 -6.8; 28 -7.1; 31 -7.4; 34 -7.6; 37 -7.8; 41 -8.0; 45 -8.2; 49 -8.4; 54 -8.6; 60 -8.8; 66 -9.1; 72 -9.4; 79 -9.7; 87 -10.1; 96 -10.4; 106 -10.7; 116 -11.0; 128 -11.2; 141 -11.4; 155 -11.5; 170 -11.5; 187 -11.6; 206 -11.5; 227 -11.4; 249 -11.2; 274 -11.1; 302 -10.9; 332 -10.6; 365 -10.2; 402 -10.0; 442 -9.8; 486 -9.5; 535 -9.2; 588 -8.9; 647 -8.5; 712 -8.1; 783 -7.7; 861 -7.3; 947 -7.3; 1042 -7.5; 1146 -8.0; 1261 -8.7; 1387 -9.1; 1526 -9.1; 1678 -9.1; 1846 -9.1; 2031 -8.5; 2234 -7.0; 2457 -4.8; 2703 -2.7; 2973 -1.6; 3270 -2.0; 3597 -1.6; 3957 -0.5; 4353 -0.5; 4788 -1.9; 5267 -2.3; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -13.1; 16529 -18.9; 18182 -15.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AAW A3H V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AAW A3H V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 182 Hz   | 0.4  | -5.1 dB  |
| Peaking | 1848 Hz  | 1.43 | -5.5 dB  |
| Peaking | 3412 Hz  | 0.85 | 6.8 dB   |
| Peaking | 6055 Hz  | 4.85 | 3.8 dB   |
| Peaking | 16981 Hz | 1.66 | -13.8 dB |
| Peaking | 16 Hz    | 1.9  | 1.0 dB   |
| Peaking | 898 Hz   | 5.57 | 0.7 dB   |
| Peaking | 8065 Hz  | 4.58 | -1.5 dB  |
| Peaking | 13944 Hz | 2.35 | 3.6 dB   |
| Peaking | 15557 Hz | 3.98 | -4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 16000 Hz | 1.41 | -10.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/AAW%20A3H%20V2/AAW%20A3H%20V2.png)