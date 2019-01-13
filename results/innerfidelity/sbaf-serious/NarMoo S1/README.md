# NarMoo S1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 21 -11.5; 23 -11.6; 25 -11.7; 28 -11.7; 31 -11.7; 34 -11.8; 37 -11.8; 41 -11.8; 45 -11.8; 49 -11.8; 54 -11.9; 60 -12.0; 66 -12.0; 72 -12.1; 79 -12.2; 87 -12.3; 96 -12.4; 106 -12.3; 116 -12.1; 128 -12.0; 141 -11.8; 155 -11.5; 170 -11.2; 187 -10.8; 206 -10.3; 227 -9.8; 249 -9.2; 274 -8.5; 302 -7.9; 332 -7.1; 365 -6.4; 402 -5.6; 442 -4.6; 486 -3.9; 535 -3.1; 588 -2.0; 647 -1.3; 712 -0.8; 783 -0.2; 861 -0.1; 947 0.2; 1042 -0.2; 1146 -0.2; 1261 -0.5; 1387 -1.3; 1526 -2.4; 1678 -3.1; 1846 -3.6; 2031 -3.8; 2234 -4.6; 2457 -5.6; 2703 -7.6; 2973 -9.3; 3270 -5.6; 3597 -2.8; 3957 -4.1; 4353 -7.7; 4788 -10.8; 5267 -6.0; 5793 -0.3; 6373 2.9; 7010 2.5; 7711 0.3; 8482 -1.9; 9330 -5.5; 10263 -6.0; 11289 -1.1; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -2.5; 20000 -2.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NarMoo S1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo S1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.2  | -11.6 dB |
| Peaking | 193 Hz   | 0.65 | -5.5 dB  |
| Peaking | 2789 Hz  | 2.24 | -8.2 dB  |
| Peaking | 4747 Hz  | 6.14 | -10.5 dB |
| Peaking | 19318 Hz | 1.46 | -3.1 dB  |
| Peaking | 900 Hz   | 1.95 | 1.7 dB   |
| Peaking | 1728 Hz  | 3.68 | -1.9 dB  |
| Peaking | 5237 Hz  | 5.03 | -3.3 dB  |
| Peaking | 6427 Hz  | 2.71 | 5.2 dB   |
| Peaking | 9726 Hz  | 4.07 | -7.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20S1/NarMoo%20S1.png)