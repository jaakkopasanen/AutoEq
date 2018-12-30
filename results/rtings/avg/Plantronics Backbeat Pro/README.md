# Plantronics Backbeat Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 -18.8; 23 -18.5; 25 -17.1; 28 -13.4; 31 -10.5; 34 -9.8; 37 -10.0; 41 -9.9; 45 -9.4; 49 -8.9; 54 -8.2; 60 -7.4; 66 -6.5; 72 -5.5; 79 -4.1; 87 -1.9; 96 0.5; 106 0.8; 116 -0.3; 128 -1.0; 141 -0.7; 155 0.3; 170 1.8; 187 3.0; 206 3.1; 227 2.3; 249 1.6; 274 1.1; 302 0.8; 332 1.0; 365 1.1; 402 1.1; 442 1.3; 486 1.1; 535 0.6; 588 0.4; 647 0.3; 712 0.1; 783 -0.0; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.1; 1261 -0.1; 1387 -0.3; 1526 -0.3; 1678 -0.0; 1846 -2.0; 2031 -3.0; 2234 -2.7; 2457 -2.1; 2703 -2.0; 2973 -2.0; 3270 -2.1; 3597 -3.5; 3957 -5.9; 4353 -6.7; 4788 -4.6; 5267 -2.4; 5793 -0.1; 6373 -1.7; 7010 -3.0; 7711 -5.5; 8482 -6.4; 9330 -5.4; 10263 -5.3; 11289 -7.2; 12418 -9.6; 13660 -11.8; 15026 -11.3; 16529 -7.0; 18182 -2.9; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plantronics Backbeat Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-33**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plantronics Backbeat Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.51 | -19.0 dB |
| Peaking | 50 Hz    | 1.91 | -6.3 dB  |
| Peaking | 4136 Hz  | 2.89 | -6.0 dB  |
| Peaking | 8261 Hz  | 4.44 | -3.7 dB  |
| Peaking | 14192 Hz | 1.04 | -12.4 dB |
| Peaking | 72 Hz    | 3.59 | -2.1 dB  |
| Peaking | 99 Hz    | 6.03 | 2.8 dB   |
| Peaking | 201 Hz   | 3.02 | 3.4 dB   |
| Peaking | 1166 Hz  | 0.15 | 0.6 dB   |
| Peaking | 2131 Hz  | 2.53 | -3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plantronics%20Backbeat%20Pro/Plantronics%20Backbeat%20Pro.png)