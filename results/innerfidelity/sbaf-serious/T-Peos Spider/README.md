# T-Peos Spider

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 21 -8.7; 23 -8.7; 25 -8.6; 28 -8.6; 31 -8.6; 34 -8.5; 37 -8.5; 41 -8.4; 45 -8.4; 49 -8.4; 54 -8.4; 60 -8.3; 66 -8.3; 72 -8.4; 79 -8.4; 87 -8.4; 96 -8.4; 106 -8.3; 116 -8.0; 128 -7.9; 141 -7.6; 155 -7.3; 170 -6.9; 187 -6.5; 206 -6.1; 227 -5.5; 249 -4.9; 274 -4.4; 302 -3.8; 332 -3.2; 365 -2.6; 402 -2.0; 442 -1.3; 486 -1.0; 535 -0.5; 588 0.2; 647 0.6; 712 0.7; 783 1.0; 861 0.7; 947 0.3; 1042 -0.1; 1146 -0.7; 1261 -1.1; 1387 -2.2; 1526 -3.2; 1678 -4.1; 1846 -4.7; 2031 -5.0; 2234 -4.6; 2457 -2.6; 2703 -0.1; 2973 3.0; 3270 5.2; 3597 5.6; 3957 3.9; 4353 -0.2; 4788 -4.7; 5267 -8.2; 5793 -3.3; 6373 0.9; 7010 1.9; 7711 -0.1; 8482 -3.4; 9330 -4.3; 10263 -1.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos Spider GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Spider ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 50 Hz    | 0.18 | -9.0 dB  |
| Peaking | 2079 Hz  | 1.08 | -17.7 dB |
| Peaking | 3119 Hz  | 0.43 | 14.9 dB  |
| Peaking | 5155 Hz  | 3.43 | -15.9 dB |
| Peaking | 9193 Hz  | 2.22 | -8.3 dB  |
| Peaking | 1372 Hz  | 2    | -2.0 dB  |
| Peaking | 3447 Hz  | 0.23 | 2.7 dB   |
| Peaking | 3866 Hz  | 0.43 | -2.6 dB  |
| Peaking | 14673 Hz | 1.08 | -1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Spider/T-Peos%20Spider.png)