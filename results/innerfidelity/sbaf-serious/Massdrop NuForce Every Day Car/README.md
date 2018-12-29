# Massdrop NuForce Every Day Car
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -12.8; 23 -12.8; 25 -12.7; 28 -12.5; 31 -12.3; 34 -12.1; 37 -11.9; 41 -11.7; 45 -11.5; 49 -11.3; 54 -11.0; 60 -10.7; 66 -10.5; 72 -10.3; 79 -10.0; 87 -9.9; 96 -9.7; 106 -9.4; 116 -8.9; 128 -8.7; 141 -8.5; 155 -8.2; 170 -7.8; 187 -7.3; 206 -6.8; 227 -6.2; 249 -5.8; 274 -5.2; 302 -4.6; 332 -4.0; 365 -3.5; 402 -2.7; 442 -2.0; 486 -1.6; 535 -1.2; 588 -0.4; 647 -0.1; 712 0.0; 783 0.3; 861 0.2; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -1.2; 1387 -1.8; 1526 -2.5; 1678 -3.1; 1846 -3.2; 2031 -3.0; 2234 -2.9; 2457 -2.2; 2703 -1.2; 2973 1.0; 3270 3.9; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.6; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop NuForce Every Day Car GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop NuForce Every Day Car ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 0.18 | -12.5 dB |
| Peaking | 182 Hz  | 0.8  | -3.4 dB  |
| Peaking | 2159 Hz | 1.53 | -5.2 dB  |
| Peaking | 4323 Hz | 1.2  | 7.8 dB   |
| Peaking | 773 Hz  | 1    | 3.9 dB   |
| Peaking | 831 Hz  | 0.55 | -2.7 dB  |
| Peaking | 2116 Hz | 5.68 | 1.2 dB   |
| Peaking | 6329 Hz | 3.6  | 4.1 dB   |
| Peaking | 7596 Hz | 1.48 | -2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20NuForce%20Every%20Day%20Car/Massdrop%20NuForce%20Every%20Day%20Car.png)