# Philips ActionFit SHQ5200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.7; 28 4.9; 31 3.9; 34 3.0; 37 2.2; 41 1.2; 45 0.4; 49 -0.2; 54 -1.0; 60 -1.6; 66 -2.2; 72 -2.7; 79 -3.2; 87 -3.6; 96 -4.0; 106 -4.0; 116 -4.2; 128 -4.3; 141 -4.4; 155 -4.4; 170 -4.2; 187 -4.0; 206 -3.9; 227 -3.6; 249 -3.2; 274 -2.8; 302 -2.5; 332 -1.6; 365 -0.4; 402 -0.7; 442 -2.7; 486 -2.1; 535 -1.5; 588 -0.9; 647 -0.6; 712 -0.6; 783 -0.1; 861 0.0; 947 0.0; 1042 0.1; 1146 0.2; 1261 0.4; 1387 0.5; 1526 0.9; 1678 1.2; 1846 2.4; 2031 2.8; 2234 3.8; 2457 2.7; 2703 2.8; 2973 4.1; 3270 5.7; 3597 6.0; 3957 5.3; 4353 2.8; 4788 2.8; 5267 5.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips ActionFit SHQ5200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips ActionFit SHQ5200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.77 | 7.1 dB  |
| Peaking | 124 Hz   | 0.36 | -4.8 dB |
| Peaking | 363 Hz   | 4.36 | 1.9 dB  |
| Peaking | 3277 Hz  | 1.17 | 5.1 dB  |
| Peaking | 5918 Hz  | 4.16 | 5.2 dB  |
| Peaking | 455 Hz   | 7.85 | -1.2 dB |
| Peaking | 2639 Hz  | 1.66 | 2.0 dB  |
| Peaking | 2726 Hz  | 4.4  | -3.5 dB |
| Peaking | 8000 Hz  | 5.68 | -1.0 dB |
| Peaking | 10044 Hz | 2.11 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20ActionFit%20SHQ5200/Philips%20ActionFit%20SHQ5200.png)