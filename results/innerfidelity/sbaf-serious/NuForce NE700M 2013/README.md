# NuForce NE700M 2013

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 21 -12.2; 23 -12.0; 25 -11.8; 28 -11.5; 31 -11.2; 34 -10.9; 37 -10.6; 41 -10.3; 45 -10.0; 49 -9.7; 54 -9.4; 60 -9.0; 66 -8.8; 72 -8.6; 79 -8.4; 87 -8.3; 96 -8.1; 106 -7.7; 116 -7.3; 128 -7.1; 141 -6.6; 155 -6.4; 170 -5.9; 187 -5.5; 206 -5.1; 227 -4.5; 249 -4.0; 274 -3.5; 302 -3.0; 332 -2.4; 365 -1.9; 402 -1.5; 442 -0.9; 486 -0.6; 535 -0.2; 588 0.4; 647 0.6; 712 0.7; 783 1.0; 861 0.7; 947 0.4; 1042 -0.2; 1146 -0.7; 1261 -1.3; 1387 -2.2; 1526 -3.3; 1678 -4.1; 1846 -4.6; 2031 -5.1; 2234 -6.0; 2457 -6.7; 2703 -7.1; 2973 -5.2; 3270 -2.2; 3597 -0.5; 3957 -1.1; 4353 -3.5; 4788 -4.6; 5267 -3.2; 5793 0.1; 6373 2.9; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.2; 11289 -0.0; 12418 0.0; 13660 -0.3; 15026 -4.7; 16529 -2.2; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NuForce NE700M 2013 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NuForce NE700M 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.2  | -11.9 dB |
| Peaking | 153 Hz   | 0.84 | -3.3 dB  |
| Peaking | 1737 Hz  | 3.18 | -2.9 dB  |
| Peaking | 2555 Hz  | 2.23 | -6.9 dB  |
| Peaking | 15338 Hz | 4.38 | -5.4 dB  |
| Peaking | 284 Hz   | 2.4  | -0.7 dB  |
| Peaking | 728 Hz   | 1.83 | 1.7 dB   |
| Peaking | 3699 Hz  | 4.22 | 3.5 dB   |
| Peaking | 4826 Hz  | 2.23 | -5.1 dB  |
| Peaking | 6453 Hz  | 3.77 | 5.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NuForce%20NE700M%202013/NuForce%20NE700M%202013.png)