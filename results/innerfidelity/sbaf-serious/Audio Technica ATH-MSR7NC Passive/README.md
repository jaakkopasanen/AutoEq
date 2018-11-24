# Audio Technica ATH-MSR7NC Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 21 0.0; 23 5.6; 25 5.2; 28 4.6; 31 4.1; 34 3.7; 37 3.4; 41 3.1; 45 2.9; 49 2.7; 54 2.5; 60 2.2; 66 2.0; 72 1.8; 79 1.6; 87 1.5; 96 1.3; 106 1.1; 116 1.1; 128 0.7; 141 0.0; 155 -0.2; 170 0.7; 187 0.1; 206 -0.0; 227 0.1; 249 0.4; 274 1.1; 302 2.0; 332 3.1; 365 4.2; 402 5.1; 442 5.6; 486 5.3; 535 4.9; 588 4.5; 647 3.7; 712 2.7; 783 2.0; 861 1.1; 947 0.4; 1042 -0.2; 1146 -0.5; 1261 -0.7; 1387 -1.8; 1526 -3.0; 1678 -3.6; 1846 -3.7; 2031 -3.5; 2234 -2.4; 2457 -0.4; 2703 1.4; 2973 3.0; 3270 3.7; 3597 4.4; 3957 3.6; 4353 -0.1; 4788 -0.5; 5267 2.2; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.4; 9330 -1.3; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-MSR7NC Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-MSR7NC Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.34 | 6.9 dB  |
| Peaking | 484 Hz  | 1.45 | 6.0 dB  |
| Peaking | 1821 Hz | 1.75 | -4.6 dB |
| Peaking | 3322 Hz | 2.84 | 5.2 dB  |
| Peaking | 6095 Hz | 5.18 | 6.6 dB  |
| Peaking | 224 Hz  | 2.02 | -1.1 dB |
| Peaking | 364 Hz  | 4.39 | 1.0 dB  |
| Peaking | 4616 Hz | 5.45 | -5.1 dB |
| Peaking | 4631 Hz | 2.06 | 2.4 dB  |
| Peaking | 9080 Hz | 4.85 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-MSR7NC%20Passive/Audio%20Technica%20ATH-MSR7NC%20Passive.png)