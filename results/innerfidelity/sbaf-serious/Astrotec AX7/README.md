# Astrotec AX7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.9; 49 5.6; 54 5.3; 60 5.0; 66 4.6; 72 4.1; 79 3.6; 87 3.1; 96 2.5; 106 2.2; 116 1.8; 128 1.4; 141 0.9; 155 0.6; 170 0.4; 187 0.1; 206 -0.2; 227 -0.2; 249 -0.4; 274 -0.4; 302 -0.5; 332 -0.5; 365 -0.4; 402 -0.3; 442 -0.1; 486 -0.1; 535 0.1; 588 0.5; 647 0.6; 712 0.6; 783 0.8; 861 0.6; 947 0.3; 1042 -0.1; 1146 -0.3; 1261 -0.8; 1387 -1.2; 1526 -1.7; 1678 -1.9; 1846 -1.8; 2031 -1.6; 2234 -1.2; 2457 0.2; 2703 2.6; 2973 5.8; 3270 6.0; 3597 6.0; 3957 5.9; 4353 1.9; 4788 1.5; 5267 3.4; 5793 4.5; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astrotec AX7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec AX7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.55 | 6.6 dB  |
| Peaking | 864 Hz   | 1.86 | 1.4 dB  |
| Peaking | 2215 Hz  | 0.79 | -4.0 dB |
| Peaking | 3276 Hz  | 1.88 | 9.3 dB  |
| Peaking | 6165 Hz  | 4.23 | 5.0 dB  |
| Peaking | 22 Hz    | 0.29 | 1.6 dB  |
| Peaking | 34 Hz    | 1.23 | -2.1 dB |
| Peaking | 224 Hz   | 0.75 | -1.0 dB |
| Peaking | 617 Hz   | 2.96 | 0.6 dB  |
| Peaking | 21748 Hz | 1.47 | -0.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Astrotec%20AX7/Astrotec%20AX7.png)