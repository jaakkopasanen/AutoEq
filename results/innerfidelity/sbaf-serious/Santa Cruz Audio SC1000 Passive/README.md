# Santa Cruz Audio SC1000 Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -0.8; 54 -1.1; 60 -1.4; 66 -1.8; 72 -2.1; 79 -2.5; 87 -2.9; 96 -3.3; 106 -3.6; 116 -3.8; 128 -4.1; 141 -4.4; 155 -4.7; 170 -4.8; 187 -4.8; 206 -5.0; 227 -4.9; 249 -5.0; 274 -5.1; 302 -5.0; 332 -5.0; 365 -5.0; 402 -5.0; 442 -4.8; 486 -4.9; 535 -4.9; 588 -4.6; 647 -4.7; 712 -5.0; 783 -5.1; 861 -5.7; 947 -6.2; 1042 -6.5; 1146 -6.7; 1261 -7.2; 1387 -8.1; 1526 -9.1; 1678 -9.9; 1846 -10.5; 2031 -11.0; 2234 -11.8; 2457 -12.5; 2703 -13.5; 2973 -13.6; 3270 -13.0; 3597 -12.4; 3957 -13.9; 4353 -18.2; 4788 -21.6; 5267 -19.7; 5793 -15.5; 6373 -13.8; 7010 -15.4; 7711 -18.8; 8482 -20.7; 9330 -19.1; 10263 -15.2; 11289 -9.3; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Santa Cruz Audio SC1000 Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Santa Cruz Audio SC1000 Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.32 | 6.2 dB   |
| Peaking | 567 Hz   | 1.06 | 2.1 dB   |
| Peaking | 4670 Hz  | 0.83 | -11.2 dB |
| Peaking | 8809 Hz  | 3.17 | -11.0 dB |
| Peaking | 22050 Hz | 2.22 | -12.1 dB |
| Peaking | 2455 Hz  | 1.65 | -1.2 dB  |
| Peaking | 3815 Hz  | 2.54 | 9.2 dB   |
| Peaking | 5013 Hz  | 1.2  | -9.3 dB  |
| Peaking | 6064 Hz  | 2.92 | 8.7 dB   |
| Peaking | 12623 Hz | 2.64 | 3.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 3.8 dB   |
| Peaking | 125 Hz   | 1.41 | 1.4 dB   |
| Peaking | 250 Hz   | 1.41 | 0.8 dB   |
| Peaking | 500 Hz   | 1.41 | 1.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -12.5 dB |
| Peaking | 16000 Hz | 1.41 | 1.9 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Santa%20Cruz%20Audio%20SC1000%20Passive/Santa%20Cruz%20Audio%20SC1000%20Passive.png)