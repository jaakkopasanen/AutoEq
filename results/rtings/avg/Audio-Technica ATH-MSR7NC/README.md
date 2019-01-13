# Audio-Technica ATH-MSR7NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 21 0.0; 23 3.3; 25 3.0; 28 2.7; 31 2.4; 34 2.3; 37 2.3; 41 2.2; 45 2.2; 49 2.1; 54 2.0; 60 1.7; 66 1.3; 72 0.9; 79 0.5; 87 -0.0; 96 -0.5; 106 -1.0; 116 -1.3; 128 -1.6; 141 -1.7; 155 -1.9; 170 -1.9; 187 -1.8; 206 -1.6; 227 -1.3; 249 -1.0; 274 -0.5; 302 0.9; 332 2.1; 365 3.3; 402 3.2; 442 2.7; 486 2.1; 535 1.7; 588 1.4; 647 1.2; 712 1.0; 783 0.8; 861 0.6; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -1.0; 1387 -1.6; 1526 -2.8; 1678 -3.9; 1846 -4.8; 2031 -5.3; 2234 -4.6; 2457 -3.1; 2703 -2.2; 2973 -1.7; 3270 -1.0; 3597 0.3; 3957 0.4; 4353 -2.9; 4788 -3.0; 5267 -1.6; 5793 0.5; 6373 1.6; 7010 -0.5; 7711 -3.4; 8482 -3.8; 9330 -2.6; 10263 -1.4; 11289 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-MSR7NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-38**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-MSR7NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.02 | 3.3 dB  |
| Peaking | 420 Hz   | 2.53 | 3.5 dB  |
| Peaking | 1990 Hz  | 2.17 | -5.6 dB |
| Peaking | 4680 Hz  | 6.49 | -3.4 dB |
| Peaking | 21080 Hz | 2.04 | -2.1 dB |
| Peaking | 56 Hz    | 2.09 | 1.4 dB  |
| Peaking | 156 Hz   | 1.34 | -2.4 dB |
| Peaking | 6515 Hz  | 3.85 | 3.7 dB  |
| Peaking | 8151 Hz  | 2.24 | -4.7 dB |
| Peaking | 11874 Hz | 2.58 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-MSR7NC/Audio-Technica%20ATH-MSR7NC.png)