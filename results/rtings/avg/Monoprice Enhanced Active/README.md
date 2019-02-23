# Monoprice Enhanced Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.1; 34 -1.5; 37 -1.8; 41 -2.2; 45 -2.5; 49 -2.7; 54 -3.0; 60 -3.5; 66 -3.9; 72 -4.2; 79 -4.5; 87 -4.7; 96 -5.1; 106 -5.5; 116 -5.7; 128 -6.1; 141 -6.3; 155 -6.6; 170 -6.8; 187 -7.2; 206 -7.7; 227 -8.2; 249 -8.6; 274 -9.1; 302 -9.6; 332 -10.1; 365 -10.5; 402 -10.9; 442 -11.0; 486 -10.9; 535 -10.2; 588 -9.1; 647 -7.6; 712 -5.8; 783 -4.3; 861 -3.3; 947 -2.6; 1042 -2.6; 1146 -2.7; 1261 -2.9; 1387 -3.0; 1526 -3.0; 1678 -3.1; 1846 -3.2; 2031 -3.2; 2234 -2.7; 2457 -2.1; 2703 -2.5; 2973 -3.9; 3270 -6.0; 3597 -8.3; 3957 -10.8; 4353 -11.9; 4788 -9.7; 5267 -6.7; 5793 -3.6; 6373 -3.0; 7010 -4.1; 7711 -7.7; 8482 -11.2; 9330 -11.0; 10263 -8.9; 11289 -6.6; 12418 -6.5; 13660 -7.3; 15026 -6.9; 16529 -6.5; 18182 -6.5; 20000 -8.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monoprice Enhanced Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice Enhanced Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.36 | 6.1 dB  |
| Peaking | 449 Hz   | 0.84 | -9.2 dB |
| Peaking | 997 Hz   | 0.37 | 6.4 dB  |
| Peaking | 4219 Hz  | 3.98 | -8.0 dB |
| Peaking | 20555 Hz | 1.88 | -3.0 dB |
| Peaking | 911 Hz   | 2.79 | 1.6 dB  |
| Peaking | 2596 Hz  | 2.6  | 3.3 dB  |
| Peaking | 2687 Hz  | 0.49 | -1.9 dB |
| Peaking | 6443 Hz  | 2.71 | 5.5 dB  |
| Peaking | 8780 Hz  | 2.94 | -6.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | -5.1 dB |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.8 dB |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Monoprice%20Enhanced%20Active/Monoprice%20Enhanced%20Active.png)