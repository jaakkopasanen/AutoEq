# Fischer Audio Equilibrium V2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -2.0; 31 -2.4; 34 -2.7; 37 -3.0; 41 -3.3; 45 -3.6; 49 -3.7; 54 -3.8; 60 -3.9; 66 -4.1; 72 -4.1; 79 -4.2; 87 -4.4; 96 -4.5; 106 -4.5; 116 -4.5; 128 -4.8; 141 -4.8; 155 -4.8; 170 -4.8; 187 -5.0; 206 -5.1; 227 -5.1; 249 -5.2; 274 -5.4; 302 -5.4; 332 -5.5; 365 -5.8; 402 -6.0; 442 -6.3; 486 -6.4; 535 -6.6; 588 -6.7; 647 -6.7; 712 -6.5; 783 -6.2; 861 -5.8; 947 -5.2; 1042 -4.4; 1146 -3.7; 1261 -3.1; 1387 -2.8; 1526 -2.7; 1678 -2.2; 1846 -1.4; 2031 -1.7; 2234 -3.5; 2457 -6.3; 2703 -9.3; 2973 -11.9; 3270 -14.3; 3597 -16.0; 3957 -17.1; 4353 -17.6; 4788 -17.1; 5267 -15.6; 5793 -13.1; 6373 -9.8; 7010 -5.8; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio Equilibrium V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Equilibrium V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 16 Hz   | 0.58 | 6.2 dB   |
| Peaking | 87 Hz   | 0.69 | 1.4 dB   |
| Peaking | 207 Hz  | 1.41 | 0.8 dB   |
| Peaking | 1822 Hz | 1.46 | 7.0 dB   |
| Peaking | 4074 Hz | 1.52 | -13.1 dB |
| Peaking | 2230 Hz | 7.77 | 1.0 dB   |
| Peaking | 3039 Hz | 2.44 | -2.9 dB  |
| Peaking | 5087 Hz | 0.9  | 4.6 dB   |
| Peaking | 5335 Hz | 2.35 | -6.9 dB  |
| Peaking | 7183 Hz | 5.22 | 2.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.7 dB   |
| Peaking | 62 Hz    | 1.41 | 1.3 dB   |
| Peaking | 125 Hz   | 1.41 | 1.3 dB   |
| Peaking | 250 Hz   | 1.41 | 1.2 dB   |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 4000 Hz  | 1.41 | -14.7 dB |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20Equilibrium%20V2/Fischer%20Audio%20Equilibrium%20V2.png)