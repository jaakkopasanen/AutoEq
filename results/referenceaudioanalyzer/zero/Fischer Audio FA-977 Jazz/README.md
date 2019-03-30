# Fischer Audio FA-977 Jazz
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.0; 23 -14.3; 25 -14.6; 28 -14.9; 31 -15.1; 34 -15.3; 37 -15.4; 41 -15.5; 45 -15.5; 49 -15.5; 54 -15.5; 60 -15.5; 66 -15.5; 72 -15.5; 79 -15.4; 87 -15.2; 96 -15.1; 106 -14.9; 116 -14.7; 128 -14.5; 141 -14.2; 155 -13.9; 170 -13.5; 187 -13.1; 206 -12.7; 227 -12.2; 249 -11.8; 274 -11.3; 302 -10.9; 332 -10.4; 365 -10.0; 402 -9.5; 442 -8.9; 486 -8.3; 535 -7.8; 588 -7.4; 647 -7.2; 712 -6.9; 783 -6.7; 861 -6.7; 947 -7.1; 1042 -7.4; 1146 -7.8; 1261 -8.1; 1387 -8.3; 1526 -8.0; 1678 -7.3; 1846 -6.1; 2031 -4.8; 2234 -3.3; 2457 -1.8; 2703 -0.6; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.3; 5267 -3.9; 5793 -5.1; 6373 -3.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio FA-977 Jazz GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio FA-977 Jazz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.39 | -7.6 dB |
| Peaking | 142 Hz  | 0.47 | -5.7 dB |
| Peaking | 1540 Hz | 1.86 | -3.4 dB |
| Peaking | 2990 Hz | 1.05 | 6.4 dB  |
| Peaking | 4445 Hz | 3.81 | 2.8 dB  |
| Peaking | 346 Hz  | 2.58 | -0.5 dB |
| Peaking | 684 Hz  | 2.38 | 0.7 dB  |
| Peaking | 5733 Hz | 7.81 | -1.1 dB |
| Peaking | 6728 Hz | 7.3  | 3.1 dB  |
| Peaking | 8064 Hz | 1.96 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.5 dB |
| Peaking | 62 Hz    | 1.41 | -6.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20FA-977%20Jazz/Fischer%20Audio%20FA-977%20Jazz.png)