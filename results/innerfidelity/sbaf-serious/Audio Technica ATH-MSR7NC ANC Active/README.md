# Audio Technica ATH-MSR7NC ANC Active
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.7; 25 5.4; 28 4.8; 31 4.3; 34 3.9; 37 3.6; 41 3.3; 45 3.1; 49 2.9; 54 2.7; 60 2.4; 66 2.2; 72 2.0; 79 1.8; 87 1.7; 96 1.5; 106 1.3; 116 1.0; 128 0.5; 141 0.1; 155 -0.2; 170 0.7; 187 -0.0; 206 -0.1; 227 -0.1; 249 0.2; 274 0.6; 302 1.4; 332 2.4; 365 3.4; 402 4.2; 442 4.7; 486 4.6; 535 4.4; 588 4.3; 647 3.7; 712 2.8; 783 2.2; 861 1.2; 947 0.5; 1042 -0.3; 1146 -0.7; 1261 -1.1; 1387 -2.4; 1526 -3.4; 1678 -3.9; 1846 -4.2; 2031 -3.9; 2234 -2.8; 2457 -0.8; 2703 0.9; 2973 2.5; 3270 3.3; 3597 3.6; 3957 2.5; 4353 -1.3; 4788 -1.6; 5267 2.1; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.7; 9330 -2.4; 10263 -0.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-MSR7NC ANC Active GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-MSR7NC ANC Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.36 | 6.2 dB  |
| Peaking | 517 Hz  | 1.35 | 5.2 dB  |
| Peaking | 1815 Hz | 1.53 | -4.9 dB |
| Peaking | 3237 Hz | 3.15 | 4.8 dB  |
| Peaking | 6084 Hz | 5.43 | 6.9 dB  |
| Peaking | 230 Hz  | 1.81 | -1.1 dB |
| Peaking | 372 Hz  | 4.3  | 1.1 dB  |
| Peaking | 4640 Hz | 5.15 | -6.2 dB |
| Peaking | 4700 Hz | 1.87 | 2.8 dB  |
| Peaking | 9247 Hz | 5.26 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-MSR7NC%20ANC%20Active/Audio%20Technica%20ATH-MSR7NC%20ANC%20Active.png)