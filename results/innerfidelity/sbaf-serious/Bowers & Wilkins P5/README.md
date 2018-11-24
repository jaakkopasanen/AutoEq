# Bowers & Wilkins P5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 21 0.0; 23 4.2; 25 4.0; 28 3.6; 31 3.2; 34 2.9; 37 2.6; 41 2.3; 45 1.9; 49 1.6; 54 1.2; 60 0.7; 66 0.1; 72 -0.5; 79 -1.1; 87 -1.8; 96 -2.6; 106 -3.1; 116 -3.5; 128 -4.3; 141 -4.7; 155 -5.1; 170 -5.1; 187 -5.4; 206 -5.5; 227 -5.3; 249 -4.9; 274 -4.1; 302 -3.0; 332 -2.1; 365 -1.2; 402 -0.5; 442 0.4; 486 0.5; 535 0.4; 588 0.6; 647 0.4; 712 0.1; 783 0.2; 861 -0.0; 947 -0.0; 1042 -0.0; 1146 -0.0; 1261 -0.2; 1387 -0.7; 1526 -1.4; 1678 -1.9; 1846 -2.3; 2031 -2.3; 2234 -3.0; 2457 -2.8; 2703 -2.0; 2973 -1.5; 3270 -0.7; 3597 0.0; 3957 1.5; 4353 1.7; 4788 2.0; 5267 2.8; 5793 3.1; 6373 3.8; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.1; 18182 -0.4; 20000 -2.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.11 | 4.4 dB  |
| Peaking | 42 Hz   | 1.8  | 1.5 dB  |
| Peaking | 175 Hz  | 0.99 | -5.9 dB |
| Peaking | 2279 Hz | 1.95 | -3.3 dB |
| Peaking | 5708 Hz | 1.9  | 3.7 dB  |
| Peaking | 175 Hz  | 2.2  | 2.4 dB  |
| Peaking | 234 Hz  | 0.85 | -2.4 dB |
| Peaking | 451 Hz  | 1.18 | 2.3 dB  |
| Peaking | 4022 Hz | 9.84 | 1.0 dB  |
| Peaking | 8356 Hz | 4.49 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P5/Bowers%20&%20Wilkins%20P5.png)